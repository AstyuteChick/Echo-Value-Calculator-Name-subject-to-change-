

import customtkinter as ctk
import v3_01_xxxxxx_evc_be as b_end


class root_win(ctk.CTk):
    def __init__(self): 
        super().__init__() 
        self.geometry("1200x675+50+50")
        self.title("Echo Value Calculator v3.01.xxxxxx")  


class SetMainFrame1(ctk.CTkFrame):
    
    def __init__(self, parent, player_char_name: ctk.StringVar, player_calc_mode: ctk.StringVar, instructs: ctk.StringVar) -> None:
        super().__init__(parent)
        char_list_ddm = ctk.CTkComboBox(
            self, 
            values = list(b_end.Character.available),
            font = ("Century Gothic", 14), 
            variable = player_char_name, 
            command = lambda event: update_instructs(instructs, player_calc_mode.get(), player_char_name.get())
        )
        title = ctk.CTkLabel(
            self,
            text = "Echo Value Calculator (name subject to change)\nv3.01.xxxxxx", 
            font = ("Cascadia Code Light", 28)
        )
        mode_ddm = ctk.CTkComboBox(
            self, 
            values = ["Normal Mode", "OverDrive Mode"], 
            font = ("Century Gothic", 14), 
            variable = player_calc_mode, 
            command = lambda event: update_instructs(instructs, player_calc_mode.get(), player_char_name.get())
        )
        char_list_ddm.pack(side = "left", expand = True, padx = 10)
        title.pack(side = "left", expand = True, padx = 10)
        mode_ddm.pack(side = "left", expand = True, padx = 10)


class SetMainFrame12(ctk.CTkFrame):

    def __init__(self, parent, tot_er: ctk.DoubleVar, er_cons: ctk.StringVar, net_er_disp: ctk.StringVar, er_cons_disp: ctk.StringVar, net_er: ctk.DoubleVar) -> None:
        super().__init__(parent)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 25)
        self.columnconfigure(2, weight = 1)
        for col in range(4): 
            self.rowconfigure(col, weight = 1)
        
        tot_er_entry = ctk.CTkEntry(
            self, 
            textvariable = tot_er, 
            font = ("Century Gothic", 14)
        )
        tot_er_entry.bind("<Key>", command = lambda event: print("Total_ER_was_inovked"))
        net_er_label = ctk.CTkLabel(
            self, 
            textvariable = net_er_disp, 
            font = ("Century Gothic", 14)
        )
        er_cons_radbut_n = ctk.CTkRadioButton(
            self, 
            text = "Normal [RECOMMENDED]]", 
            font = ("Century Gothic", 14), 
            variable = er_cons,
            value = "n", 
            command = lambda: update_er_cons_disp(er_cons_disp, er_cons.get())
        )
        er_cons_radbut_y = ctk.CTkRadioButton(
            self, 
            text = "Outro Buff (Zhezhi / Yangyang)", 
            font = ("Century Gothic", 14), 
            variable = er_cons,
            value = "y", 
            command = lambda: update_er_cons_disp(er_cons_disp, er_cons.get())
        )
        er_cons_radbut_x = ctk.CTkRadioButton(
            self, 
            text = "Ignore ER requirements [NOT RECOMMENDED]", 
            font = ("Century Gothic", 14), 
            variable = er_cons, 
            value = "x", 
            command = lambda: update_er_cons_disp(er_cons_disp, er_cons.get())
        )
        er_cons_selected = ctk.CTkLabel(
            self, 
            textvariable = er_cons_disp, 
            font = ("Century Gothic", 14)
        )

        tot_er_entry.grid(row = 1, column = 0, sticky = "nsw", padx = 10)
        net_er_label.grid(row = 2, column = 0, sticky = "nsw", padx = 10)
        er_cons_radbut_n.grid(row = 0, column = 2, sticky = "nsw", padx = 10)
        er_cons_radbut_y.grid(row = 1, column = 2, sticky = "nsw", padx = 10)
        er_cons_radbut_x.grid(row = 2, column = 2, sticky = "nsw", padx = 10)
        er_cons_selected.grid(row = 3, column = 2, sticky = "nsw", padx = 10)


class SetMainFrame2(ctk.CTkFrame):
    
    def __init__(self, parent, player_char_name, player_calc_mode, instructs, player_entry_fa1, player_entry_fa2, player_entry_fa3, player_entry_fa4, player_entry_fa5, player_entry_ba, player_entry_ea):
        super().__init__(parent)

        calc_tabs = ctk.CTkTabview(self)

        calc_tabs.add("Instructions")
        calc_tabs.add("Full Evaluation")
        calc_tabs.add("Build Evaluation")
        calc_tabs.add("Echo Evaluation")
        calc_tabs.add("Scoring Method")
        calc_tabs.add("Rating Brackets")
        calc_tabs.add("Display Data")

        tab1 = DisplayTab(calc_tabs.tab("Instructions"), instructs)
        tab1.pack(expand = True, fill = "both")

        tab2 = ctk.CTkScrollableFrame(calc_tabs.tab("Full Evaluation"), orientation = "vertical")

        tab21 = ctk.CTkScrollableFrame(tab2, orientation = "horizontal")
        tab211 = EchoCell(tab21, player_entry_fa1)
        tab212 = EchoCell(tab21, player_entry_fa2)
        tab213 = EchoCell(tab21, player_entry_fa3)
        tab214 = EchoCell(tab21, player_entry_fa4)
        tab215 = EchoCell(tab21, player_entry_fa5)
        tab211.pack(side = "left")
        tab212.pack(side = "left")
        tab213.pack(side = "left")
        tab214.pack(side = "left")
        tab215.pack(side = "left")
        tab21.pack(expand = True, fill = "both")

        tab22 = ctk.CTkFrame(tab2)
        tab2_calc_but = ctk.CTkButton(tab22, text = "Calculate Echo and Build Value", command = lambda: print("Calc_Tab2_pressed. "), font = ("Century Gothic", 14))
        disp_val_2 = ctk.CTkLabel(tab22, text = "Total Value: ", font = ("Century Gothic", 14))
        tab2_calc_but.pack(side = "left", padx = 10, pady = 25)
        disp_val_2.pack(side = "left", padx = 10, pady = 25)
        tab22.pack()

        tab2.pack(expand = True, fill = "both")

        tab3 = ctk.CTkFrame(calc_tabs.tab("Build Evaluation"))
        tab31 = EchoCell(tab3, player_entry_ba)
        tab31.pack(expand = True, fill = "both")
        tab32 = ctk.CTkFrame(tab3)
        tab3_calc_but = ctk.CTkButton(tab32, text="Calculate Echo and Build Value", command=lambda: print("Calc_Tab2_pressed. "), font=("Century Gothic", 14))
        disp_val_3 = ctk.CTkLabel(tab32, text="Total Value: ", font=("Century Gothic", 14))
        tab3_calc_but.pack(side="left", padx=10, pady=25)
        disp_val_3.pack(side="left", padx=10, pady=25)
        tab32.pack()

        tab3.pack(expand = True, fill = "both")

        tab4 = ctk.CTkFrame(calc_tabs.tab("Echo Evaluation"))
        tab41 = EchoCell(tab4, player_entry_ea)
        tab41.pack(expand=True, fill="both")
        tab42 = ctk.CTkFrame(tab4)
        tab4_calc_but = ctk.CTkButton(tab42, text="Calculate Echo and Build Value", command=lambda: print("Calc_Tab2_pressed. "), font=("Century Gothic", 14))
        disp_val_4 = ctk.CTkLabel(tab42, text="Total Value: ", font=("Century Gothic", 14))
        tab4_calc_but.pack(side="left", padx=10, pady=25)
        disp_val_4.pack(side="left", padx=10, pady=25)
        tab42.pack()
        tab4.pack(expand = True, fill = "both")

        tab5 = DisplayTab(calc_tabs.tab("Scoring Method"), instructs)
        tab5.pack(expand = True, fill = "both")

        tab6 = DisplayTab(calc_tabs.tab("Rating Brackets"), instructs)
        tab6.pack(expand = True, fill = "both")

        disp_data_tabs = ctk.CTkTabview(calc_tabs.tab("Display Data"))

        disp_data_tabs.add("General Assumptions")
        disp_data_tabs.add("Character Specific Assumptions")
        disp_data_tabs.add("General Data")
        disp_data_tabs.add("Character Specific Data")
        disp_data_tabs.add("Test Crit Ratio")
        disp_data_tabs.add("Character building sequence for optimized time")

        tab71 = DisplayTab(disp_data_tabs.tab("General Assumptions"), instructs)
        tab72 = DisplayTab(disp_data_tabs.tab("Character Specific Assumptions"), instructs)
        tab73 = DisplayTab(disp_data_tabs.tab("General Data"), instructs)
        tab74 = DisplayTab(disp_data_tabs.tab("Character Specific Data"), instructs)
        disp_data_tabs.tab("Test Crit Ratio").columnconfigure(0, weight = 1)
        disp_data_tabs.tab("Test Crit Ratio").columnconfigure(1, weight = 1)
        for line in range (6):
            disp_data_tabs.tab("Test Crit Ratio").rowconfigure(line, weight = 1)
        tcr_cr_label = ctk.CTkLabel(disp_data_tabs.tab("Test Crit Ratio"), text = "Enter your character's crit rate % here: ")
        tcr_cd_label = ctk.CTkLabel(disp_data_tabs.tab("Test Crit Ratio"), text = "Enter your character's crit damage % here: ")
        tcr_cr_entry = ctk.CTkEntry(disp_data_tabs.tab("Test Crit Ratio"))
        tcr_cd_entry = ctk.CTkEntry(disp_data_tabs.tab("Test Crit Ratio"))
        tcr_cr_label.grid(row = 0, column = 0, sticky = "nsew")
        tcr_cr_entry.grid(row = 0, column = 1, sticky = "nsew")
        tcr_cd_label.grid(row = 1, column = 0, sticky = "nsew")
        tcr_cd_entry.grid(row = 1, column = 1, sticky = "nsew")
        tcr_result = ctk.CTkLabel(disp_data_tabs.tab("Test Crit Ratio"), text = "Your Crit Ratio is: ")
        tcr_result.grid(row = 4, column = 0)
        tab76 = DisplayTab(disp_data_tabs.tab("Character building sequence for optimized time"), instructs)

        tab71.pack(expand = True, fill = "both")
        tab72.pack(expand = True, fill = "both")
        tab73.pack(expand = True, fill = "both")
        tab74.pack(expand = True, fill = "both")
        tab76.pack(expand = True, fill = "both")
        disp_data_tabs.pack(expand = True, fill = "both")

        calc_tabs.pack(expand = True, fill = "both")


class DisplayTab(ctk.CTkScrollableFrame):

    def __init__(self, parent, disp_txt, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        disp_label = ctk.CTkLabel(self, textvariable = disp_txt, font = ("Century Gothic", 14))
        disp_label.pack(expand = True, fill = "both")


class EchoCell(ctk.CTkFrame):

    def __init__(self, parent, entry_list):
        super().__init__(parent)
        cr_label = ctk.CTkLabel(self, text = "Crit Rate% : ", font = ("Century Gothic", 14))
        cd_label = ctk.CTkLabel(self, text = "Crit Damage% : ", font = ("Century Gothic", 14))
        atk_label = ctk.CTkLabel(self, text = "Attack% : ", font = ("Century Gothic", 14))
        fatk_label = ctk.CTkLabel(self, text = "Attack : ", font = ("Century Gothic", 14))
        hp_label = ctk.CTkLabel(self, text = "HP% : ", font = ("Century Gothic", 14))
        fhp_label = ctk.CTkLabel(self, text = "Flat HP : ", font = ("Century Gothic", 14))
        def_label = ctk.CTkLabel(self, text = "Defense% : ", font = ("Century Gothic", 14))
        fdef_label = ctk.CTkLabel(self, text = "Defense : ", font = ("Century Gothic", 14))
        ba_label = ctk.CTkLabel(self, text = "Basic Attack Damage% : ", font = ("Century Gothic", 14))
        ha_label = ctk.CTkLabel(self, text = "Heavy Attack Damage% : ", font = ("Century Gothic", 14))
        skill_label = ctk.CTkLabel(self, text = "Resonance Skill Damage% : ", font = ("Century Gothic", 14))
        lib_label = ctk.CTkLabel(self, text = "Resonance Liberation Damage% : ", font = ("Century Gothic", 14))
        er_label = ctk.CTkLabel(self, text = "Energy Regen% : ", font = ("Century Gothic", 14))

        self.cr_entry = ctk.CTkEntry(self, textvariable = entry_list[0])
        self.cd_entry = ctk.CTkEntry(self, textvariable = entry_list[1])
        self.atk_entry = ctk.CTkEntry(self, textvariable = entry_list[2])
        self.fatk_entry = ctk.CTkEntry(self, textvariable = entry_list[3])
        self.hp_entry = ctk.CTkEntry(self, textvariable = entry_list[4])
        self.fhp_entry = ctk.CTkEntry(self, textvariable = entry_list[5])
        self.def_entry = ctk.CTkEntry(self, textvariable = entry_list[6])
        self.fdef_entry = ctk.CTkEntry(self, textvariable = entry_list[7])
        self.ba_entry = ctk.CTkEntry(self, textvariable = entry_list[8])
        self.ha_entry = ctk.CTkEntry(self, textvariable = entry_list[9])
        self.skill_entry = ctk.CTkEntry(self, textvariable = entry_list[10])
        self.lib_entry = ctk.CTkEntry(self, textvariable = entry_list[11])
        self.er_entry = ctk.CTkEntry(self, textvariable = entry_list[12])

        self.columnconfigure(0, weight = 3)
        self.columnconfigure(1, weight = 1)
        for line in range(13):
            self.rowconfigure(line, weight = 1)
        
        cr_label.grid(row = 0, column = 0)
        self.cr_entry.grid(row = 0, column = 1, sticky = "nsw")
        cd_label.grid(row = 1, column = 0)
        self.cd_entry.grid(row = 1, column = 1, sticky = "nsw")
        atk_label.grid(row = 2, column = 0)
        self.atk_entry.grid(row = 2, column = 1, sticky = "nsw")
        fatk_label.grid(row = 3, column = 0)
        self.fatk_entry.grid(row = 3, column = 1, sticky = "nsw")
        hp_label.grid(row = 4, column = 0)
        self.hp_entry.grid(row = 4, column = 1, sticky = "nsw")
        fhp_label.grid(row = 5, column = 0)
        self.fhp_entry.grid(row = 5, column = 1, sticky = "nsw")
        def_label.grid(row = 6, column = 0)
        self.def_entry.grid(row = 6, column = 1, sticky = "nsw")
        fdef_label.grid(row = 7, column = 0)
        self.fdef_entry.grid(row = 7, column = 1, sticky = "nsw")
        ba_label.grid(row = 8, column = 0)
        self.ba_entry.grid(row = 8, column = 1, sticky = "nsw")
        ha_label.grid(row = 9, column = 0)
        self.ha_entry.grid(row = 9, column = 1, sticky = "nsw")
        skill_label.grid(row = 10, column = 0)
        self.skill_entry.grid(row = 10, column = 1, sticky = "nsw")
        lib_label.grid(row = 11, column = 0)
        self.lib_entry.grid(row = 11, column = 1, sticky = "nsw")
        er_label.grid(row = 12, column = 0)
        self.er_entry.grid(row = 12, column = 1, sticky = "nsw")


class SetMainFrame3(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        exit_but = ctk.CTkButton(self, text = "Close Echo Value Calculator (nstc)", font = ("Century Gothic", 14))
        exit_but.pack()


def main():

    root = root_win()

    player_char_name = ctk.StringVar(value="Carlotta")
    player_calc_mode = ctk.StringVar(value="Normal Mode")
    player_entry_fa1 = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_entry_fa2 = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_entry_fa3 = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_entry_fa4 = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_entry_fa5 = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_entry_ba = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_entry_ea = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    player_tcr_cr = ctk.DoubleVar(value = 50.0)
    player_tcr_cd = ctk.DoubleVar(value = 200.0)
    tot_er = ctk.DoubleVar(value = 100.0)
    er_cons = ctk.StringVar(value = "n")
    net_er = ctk.DoubleVar()
    stat_medians = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                    ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    echo_mainstats = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                      ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    char_data = [ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), 
                 ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()]
    instructs = ctk.StringVar(value = b_end.display_menu(player_calc_mode.get(), player_char_name.get()))
    net_er_disp = ctk.StringVar(value = "Net ER% : " + str(net_er))
    er_cons_disp = ctk.StringVar(value = "Option selected: Normal Mode")

    main_frame1 = SetMainFrame1(root, player_char_name, player_calc_mode, instructs)
    main_frame12 = SetMainFrame12(root, tot_er, er_cons, net_er_disp, er_cons_disp, net_er)
    main_frame2 = SetMainFrame2(root, player_char_name, player_calc_mode, instructs)
    main_frame3 = SetMainFrame3(root)
    main_frame1.pack(expand = True, fill = "x")
    main_frame12.pack(fill = "x")
    main_frame2.pack(expand = True, fill = "both")
    main_frame3.pack(pady = 25)

    root.mainloop()


def update_instructs(instructs_ui: ctk.StringVar, calc_mode: str, char_name: str) -> None:
    instructs_ui.set(b_end.display_menu(calc_mode, char_name))
    

def update_er_cons_disp(er_cons_disp, er_cons):
    if er_cons == "y": er_os = "Outro buff (Zhezhi / Yangyang)"
    elif er_cons == "n": er_os = "Normal Mode"
    else: er_os = "ER% Not considered"
    er_cons_disp.set("Option selected: " + er_os)

def update_net_er(net_er, tot_er, net_er_disp):
    net_er.set(tot_er - 125)
    net_er_disp.set("Net ER% : " + str(net_er))


if __name__ == "__main__":
    main()
    
