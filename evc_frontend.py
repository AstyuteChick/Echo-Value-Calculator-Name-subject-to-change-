

import customtkinter as ctk
from v3_01_Echo_Value_Calculator_nstc_source_code import Character, disp_menu_tkinter


class root_win(ctk.CTk):
    def __init__(self): 
        super().__init__() 
        self.geometry("1200x675")
        self.title("Echo Value Calculator v3.01.xxxxxx")  


class SetMainFrame1(ctk.CTkFrame):
    
    def __init__(self, parent, player_char_name, player_calc_mode, instructs):
        super().__init__(parent)
        char_list_ddm = ctk.CTkComboBox(
            self, 
            values = list(Character.available),
            font = ("Century Gothic", 18), 
            variable = player_char_name, 
            command=set_disp_txt(player_char_name, player_calc_mode, instructs)
            )
        title = ctk.CTkLabel(
            self,
            text = "Echo Value Calculator", 
            font = ("Cascadia Code Light", 36)
            )
        mode_button = ctk.CTkComboBox(
            self, 
            values = ["Normal Mode", "OverDrive Mode"], 
            font = ("Century Gothic", 18), 
            variable = player_calc_mode
            )
        char_list_ddm.pack(side = "left", expand = True)
        title.pack(side = "left", expand = True)
        mode_button.pack(side = "left", expand = True)


def set_disp_txt(player_char_name, player_calc_mode, instructs):
    instructs.set(disp_menu_tkinter(player_calc_mode.get(), player_char_name.get()))


class SetMainFrame2(ctk.CTkFrame):
    
    def __init__(self, parent, player_char_name, player_calc_mode, instructs):
        super().__init__(parent)

        calc_tabs = ctk.CTkTabview(self)
        calc_tabs.pack(expand = True, fill = "both")

        calc_tabs.add("Instructions")
        calc_tabs.add("Full Evaluation")
        calc_tabs.add("Build Evaluation")
        calc_tabs.add("Echo Evaluation")
        calc_tabs.add("Scoring Method")
        calc_tabs.add("Rating Brackets")
        calc_tabs.add("Display Data")

        tab1 = DisplayTab(calc_tabs.tab("Instructions"), instructs)
        tab1.pack(expand = True, fill = "both")

        tab2 = ctk.CTkScrollableFrame(calc_tabs.tab("Full Evaluation"), orientation = "horizontal")
        tab21 = EchoCell(tab2)
        tab22 = EchoCell(tab2)
        tab23 = EchoCell(tab2)
        tab24 = EchoCell(tab2)
        tab25 = EchoCell(tab2)
        tab21.pack(side = "left")
        tab22.pack(side = "left")
        tab23.pack(side = "left")
        tab24.pack(side = "left")
        tab25.pack(side = "left")
        tab2.pack(expand = True, fill = "both")

        tab3 = EchoCell(calc_tabs.tab("Build Evaluation"))
        tab3.pack()

        tab4 = EchoCell(calc_tabs.tab("Echo Evaluation"))
        tab4.pack()

        tab5 = DisplayTab(calc_tabs.tab("Scoring Method"), instructs)
        tab5.pack(expand = True, fill = "both")

        tab6 = DisplayTab(calc_tabs.tab("Rating Brackets"), instructs)
        tab6.pack(expand = True, fill = "both")

        disp_data_tabs = ctk.CTkTabview(calc_tabs.tab("Display Data"))
        disp_data_tabs.pack(expand = True, fill = "both")

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


class DisplayTab(ctk.CTkScrollableFrame):

    def __init__(self, parent, disp_txt, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        disp_label = ctk.CTkLabel(self, textvariable = disp_txt, font = ("Century Gothic", 18))
        disp_label.pack(expand = True, fill = "both")


class EchoCell(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        cr_label = ctk.CTkLabel(self, text = "Crit Rate% : ", font = ("Century Gothic", 18))
        cd_label = ctk.CTkLabel(self, text = "Crit Damage% : ", font = ("Century Gothic", 18))
        atk_label = ctk.CTkLabel(self, text = "Attack% : ", font = ("Century Gothic", 18))
        fatk_label = ctk.CTkLabel(self, text = "Attack : ", font = ("Century Gothic", 18))
        hp_label = ctk.CTkLabel(self, text = "HP% : ", font = ("Century Gothic", 18))
        fhp_label = ctk.CTkLabel(self, text = "Flat HP : ", font = ("Century Gothic", 18))
        def_label = ctk.CTkLabel(self, text = "Defense% : ", font = ("Century Gothic", 18))
        fdef_label = ctk.CTkLabel(self, text = "Defense : ", font = ("Century Gothic", 18))
        ba_label = ctk.CTkLabel(self, text = "Basic Attack Damage% : ", font = ("Century Gothic", 18))
        ha_label = ctk.CTkLabel(self, text = "Heavy Attack Damage% : ", font = ("Century Gothic", 18))
        skill_label = ctk.CTkLabel(self, text = "Resonance Skill Damage% : ", font = ("Century Gothic", 18))
        lib_label = ctk.CTkLabel(self, text = "Resonance Liberation Damage% : ", font = ("Century Gothic", 18))
        er_label = ctk.CTkLabel(self, text = "Energy Regen% : ", font = ("Century Gothic", 18))

        cr_entry = ctk.CTkEntry(self)
        cd_entry = ctk.CTkEntry(self)
        atk_entry = ctk.CTkEntry(self)
        fatk_entry = ctk.CTkEntry(self)
        hp_entry = ctk.CTkEntry(self)
        fhp_entry = ctk.CTkEntry(self)
        def_entry = ctk.CTkEntry(self)
        fdef_entry = ctk.CTkEntry(self)
        ba_entry = ctk.CTkEntry(self)
        ha_entry = ctk.CTkEntry(self)
        skill_entry = ctk.CTkEntry(self)
        lib_entry = ctk.CTkEntry(self)
        er_entry = ctk.CTkEntry(self)

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        for line in range(13):
            self.rowconfigure(line, weight = 1)
        
        cr_label.grid(row = 0, column = 0, sticky = "nsew")
        cr_entry.grid(row = 0, column = 1, sticky = "nsew")
        cd_label.grid(row = 1, column = 0, sticky = "nsew")
        cd_entry.grid(row = 1, column = 1, sticky = "nsew")
        atk_label.grid(row = 2, column = 0, sticky = "nsew")
        atk_entry.grid(row = 2, column = 1, sticky = "nsew")
        fatk_label.grid(row = 3, column = 0, sticky = "nsew")
        fatk_entry.grid(row = 3, column = 1, sticky = "nsew")
        hp_label.grid(row = 4, column = 0, sticky = "nsew")
        hp_entry.grid(row = 4, column = 1, sticky = "nsew")
        fhp_label.grid(row = 5, column = 0, sticky = "nsew")
        fhp_entry.grid(row = 5, column = 1, sticky = "nsew")
        def_label.grid(row = 6, column = 0, sticky = "nsew")
        def_entry.grid(row = 6, column = 1, sticky = "nsew")
        fdef_label.grid(row = 7, column = 0, sticky = "nsew")
        fdef_entry.grid(row = 7, column = 1, sticky = "nsew")
        ba_label.grid(row = 8, column = 0, sticky = "nsew")
        ba_entry.grid(row = 8, column = 1, sticky = "nsew")
        ha_label.grid(row = 9, column = 0, sticky = "nsew")
        ha_entry.grid(row = 9, column = 1, sticky = "nsew")
        skill_label.grid(row = 10, column = 0, sticky = "nsew")
        skill_entry.grid(row = 10, column = 1, sticky = "nsew")
        lib_label.grid(row = 11, column = 0, sticky = "nsew")
        lib_entry.grid(row = 11, column = 1, sticky = "nsew")
        er_label.grid(row = 12, column = 0, sticky = "nsew")
        er_entry.grid(row = 12, column = 1, sticky = "nsew")


class SetMainFrame3(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        exit_but = ctk.CTkButton(self, text = "Close Echo Value Calculator (nstc)")
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
    player_tcr_cr = ctk.DoubleVar()
    player_tcr_cd = ctk.DoubleVar()
    instructs = ctk.StringVar(value = disp_menu_tkinter(player_calc_mode.get(), player_char_name.get()))

    main_frame1 = SetMainFrame1(root, player_char_name, player_calc_mode, instructs)
    main_frame2 = SetMainFrame2(root, player_char_name, player_calc_mode, instructs)
    main_frame3 = SetMainFrame3(root)
    main_frame1.pack(fill = "x")
    main_frame2.pack(expand = True, fill = "both")    
    main_frame3.pack(pady = 50)

    root.mainloop()


if __name__ == "__main__":
    main()
    

