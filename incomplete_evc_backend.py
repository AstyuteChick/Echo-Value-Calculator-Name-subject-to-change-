import heapq

class GameData:

    rel_val_stat_names=["Crit Rate(%)", "Crit Damage(%)", "Atk(%)", "Flat Atk", "HP(%)", "Flat HP", "Def(%)", "Flat Def", "Basic(%)", "Heavy(%)", "Skill(%)", "Liberation(%)"]
    er_stat_names=["Required ER", "ER Importance", "Resonance Cost"]
    substat_names=["Crit Rate(%)", "Crit Damage(%)", "Atk(%)", "Flat Atk", "HP(%)", "Flat HP", "Def(%)", "Flat Def", "Basic(%)", "Heavy(%)", "Skill(%)", "Liberation(%)", "ER(%)"]
    substat_medians=[8.4, 16.8, 9.0, 45.0, 9.0, 450.0, 11.35, 55.0, 9.0, 9.0, 9.0, 9.0, 9.6]
    substat_max=[10.5, 21.0, 11.6, 60.0, 11.6, 580.0, 14.7, 70.0, 11.6, 11.6, 11.6, 11.6, 12.4]

    def __init__(self, mode: str): self.ssm=mode

    @property
    def ssm(self)-> dict: return self._ssm
    @ssm.setter
    def ssm(self, mode: str)-> None:
        ssm_dict={}
        if mode=="O":
            for i in range(13): ssm_dict[GameData.substat_names[i]]=GameData.substat_max[i]
        else: 
            for i in range(13): ssm_dict[GameData.substat_names[i]]=GameData.substat_medians[i]
        self._ssm=ssm_dict

class Character:

    data: dict[str, list]={
        #Name:          [[cr, cd, atk%, atk, hp%, hp, def%, def, ba%, ha%, skill%, liberation%], [req_er, imp_er, rc], analysis]
        "Carlotta":     [[1.0, 1.0, 0.5, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5*0.85, 0.0], [125.0, 0.5, 125.0], True]
    }

    def __init__(self, name: str)-> None:
        self.name=name
        self.rv=Character.data[self.name][0]
        self.er=Character.data[self.name][1]
        self.anal=Character.data[self.name][2]

    @property
    def name(self)-> str: return self._name
    @name.setter
    def name(self, name: str)-> None:
        char_found=False
        for char_name in Character.data:
            if char_name==name:
                char_found=True
                break
        if char_found!=True: raise ValueError("Character not found")
        self._name=name
    
    @property
    def rv(self)-> dict: return self._rv
    @rv.setter
    def rv(self, rv_list: list)-> None:
        rv_dict={}
        for index in range(12): rv_dict[GameData.rel_val_stat_names[index]]=rv_list[index]
        self._rv=rv_dict

    @property
    def er(self)-> dict: return self._er
    @er.setter
    def er(self, er_list: list)-> None:
        er_dict={}
        for index in range(3): er_dict[GameData.er_stat_names[index]]=er_list[index]
        self._er=er_dict

class Echo:

    def __init__(self, ssr_in: list)-> None: self.ssr=ssr_in

    @property
    def ssr(self)-> dict: return self._ssr
    @ssr.setter
    def ssr(self, ssr_in: list) -> None:
        ssr_data={}
        index=0
        for stat_name in GameData.substat_names:
            ssr_data[stat_name]=ssr_in[index]
            index=index+1
        if len(ssr_data)!=13: raise ValueError("Invalid Echo substat data: "+str(len(ssr_data)))
        stat_count=0
        for substat in ssr_data:
            if ssr_data[substat]!=0: stat_count=stat_count+1
        if stat_count>5: raise ValueError("Too many sub stats: "+str(stat_count))
        self._ssr=ssr_data

def av_er(er_net_av: float, er_ssr: float, er_med: float, er_imp: float)-> tuple[float, float]:
    if er_net_av<0: er_av=(er_ssr/er_med)*er_imp
    else:
        er_net_av=er_net_av-er_ssr
        if er_net_av<0: 
            er_av=(-er_net_av/er_med)*er_imp
            er_net_av=0
        else: er_av=0
    return er_net_av, er_av

def ep_er(er_net_ep: float, er_ssr: float, er_med: float, er_imp: float)-> tuple[float, float]:
    if er_net_ep<0:
        if er_net_ep/er_med<=-1: 
            er_ep=er_imp
            er_net_ep=er_net_ep+er_med
        else:
            er_ep=((-er_net_ep)/er_med)*er_imp
            er_net_ep=0
    else:
        er_net_ep=er_net_ep-er_ssr
        if er_net_ep<0:
            if er_net_ep/er_med<=-1: 
                er_ep=er_imp
                er_net_ep=er_net_ep+er_med
            else:
                er_ep=((-er_net_ep)/er_med)*er_imp
                er_net_ep=0
        else: er_ep=0
    return er_net_ep, er_ep

def av_stats(echo_ssr: dict, ssm: dict, char_player: Character, er_net_av: float)-> tuple[float, float]:
    er_net_av, total_av=av_er(er_net_av, echo_ssr["ER(%)"], ssm["ER(%)"], char_player.er[1])
    for substat in echo_ssr: 
        if substat!="ER(%)": total_av=total_av+((echo_ssr[substat]/ssm[substat])*char_player.rv[substat])
    return total_av, er_net_av

def ep_stats(echo_ssr: dict, ssm: dict, char_player: Character, er_net_ep: float)-> tuple[float, float]:
    rel_pot_vals=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    er_net_ep, rel_pot_vals[12]=ep_er(er_net_ep, echo_ssr["ER(%)"], ssm["ER(%)"], char_player.er[1])
    index=0
    for substat in char_player.rv: 
        rel_pot_vals[index]=char_player.rv[substat]
        index=index+1
        if index==11: break
    return sum(heapq.nlargest(5, rel_pot_vals)), er_net_ep

def adjust_req_er(er_req, rc, buff_val): return er_req*(1-(buff_val/rc))

def es_stats(av_total: float, ep_total: float): return av_total/ep_total

def main():

    while True:

        char_player=Character(input("Enter Character: ").strip().lower().capitalize())

        if char_player.er[0]!=0 and char_player.er[0]>100:
            outro_buff=input("Enter Y for Yangyang, Z for Zhezhi, or enter any key to continue: ").strip().upper()
            if outro_buff=="Y": char_player.er[0]=adjust_req_er(char_player.er[0], char_player.er[2], 20)
            elif outro_buff=="Z": char_player.er[0]=adjust_req_er(char_player.er[0], char_player.er[2], 15)
            er_build=float(input("Enter total ER of your build (make sure correct weapons and echoes are equipped, and character is deployed): "))
            er_net=er_build-char_player.er[0]
        else: er_net=0
        er_net_av=er_net
        er_net_ep=er_net

        calc_mode=input("Enter O for overdrive mode, otherwise enter any key to continue: ").strip().upper()
        ssgd=GameData(calc_mode)

        ssr=[]
        for i in range(12): 
            if char_player.rv[GameData.substat_names[i]]!=0: ssr.append(float(input(f"Enter {GameData.substat_names[i]} substat roll amount: ")))
            else: ssr.append(0.0)
        if char_player.er[0]!=0 and char_player.er[0]>100: ssr.append(float(input(f"Enter {GameData.substat_names[12]} substat roll amount: ")))
        else: ssr.append(0.0)
        echo_player=Echo(ssr)

        av_total, er_net_av=av_stats(echo_player.ssr, ssgd.ssm, char_player, er_net_av)
        ep_total, er_net_ep=ep_stats(echo_player.ssr, ssgd.ssm, char_player, er_net_ep)
        es_total=es_stats(av_total, ep_total)

        print(es_total)

if __name__=="__main__": main()
