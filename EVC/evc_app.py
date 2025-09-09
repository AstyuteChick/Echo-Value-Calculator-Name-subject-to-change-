from flask import Flask, render_template, request, url_for, redirect
from evc_engine import *

evc_app=Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")

@evc_app.route("/")
def home(): return redirect(url_for("echo"))

@evc_app.route("/echo", methods=["GET", "POST"])
def echo():
    if request.method == "GET":
        return render_template("echo.html", stat_names=GameData.substat_names, stat_rolls=GameData.substat_rolls, char_data=Character.data, echo_score="0.0", 
                               echo_tier="Echo tier for the above Echo score. ", prev_char="Carlotta", prev_er="100", prev_buff="None")
    elif request.method == "POST":
        try: 
            es, et = main(request.form["char_echo"], 
                          request.form["buff_echo"], 
                          request.form["er_tot_echo"], 
                          [request.form["Crit Rate(%)"], request.form["Crit Damage(%)"], request.form["Atk(%)"], request.form["Flat Atk"], request.form["HP(%)"], request.form["Flat HP"], 
                           request.form["Def(%)"], request.form["Flat Def"], request.form["Basic(%)"], request.form["Heavy(%)"], request.form["Skill(%)"], request.form["Liberation(%)"], 
                           request.form["ER(%)"]], 
                           "echo")
            return render_template("echo.html", stat_names=GameData.substat_names, stat_rolls=GameData.substat_rolls, char_data=Character.data, echo_score=es, echo_tier=et, 
                                   prev_char=request.form["char_echo"], prev_er=request.form["er_tot_echo"], prev_buff=request.form["buff_echo"])
        except Exception as msg: return f"<h1>Error 69_420: </h1><br><h2>{msg}</h2><br><p>Site is under contruction and not yet fully complete. Forwarding the above error name to me ('AstyuteChick' at Reddit and GitHub) would be of great help!</p>"
    else: raise ValueError

@evc_app.route("/build", methods=["GET", "POST"])
def build():
    if request.method == "GET":
        return render_template("build.html", stat_names=GameData.substat_names, char_data=Character.data, echo_score="Build Score", echo_tier="Build Tier", prev_char="Carlotta", 
                                   prev_er="100", prev_buff="None", mainstat_dict=GameData.mainstat_vals)
    elif request.method == "POST":
        try: 
            if request.form["echo_setup"]=="43311": 
                echo_costs=[4, 3, 3, 1, 1]
                echo_mainstats=[request.form["s1"], request.form["s2"], request.form["s3"], request.form["s4"], request.form["s5"]]
            else: 
                echo_costs=[4, 4, 1, 1, 1]
                echo_mainstats=[request.form["c1"], request.form["c2"], request.form["c3"], request.form["c4"], request.form["c5"]]
            es, et = main(request.form["char_build"], 
                          request.form["buff_build"], 
                          request.form["er_tot_build"], 
                          [request.form["Crit Rate(%)"], request.form["Crit Damage(%)"], request.form["Atk(%)"], request.form["Flat Atk"], request.form["HP(%)"], request.form["Flat HP"], 
                           request.form["Def(%)"], request.form["Flat Def"], request.form["Basic(%)"], request.form["Heavy(%)"], request.form["Skill(%)"], request.form["Liberation(%)"], 
                           request.form["ER(%)"]], 
                           "build", {"echo_cost": echo_costs, "echo_mainstat": echo_mainstats})
            return render_template("build.html", stat_names=GameData.substat_names, char_data=Character.data, echo_score=es, echo_tier=et, prev_char=request.form["char_build"], 
                                   prev_er=request.form["er_tot_build"], prev_buff=request.form["buff_build"], mainstat_dict=GameData.mainstat_vals)
        except Exception as msg: return f"Error in build post: {msg}"
    else: raise ValueError

@evc_app.route("/full", methods=["GET", "POST"])
def full():
    if request.method == "GET":
        return render_template("full.html", stat_names=GameData.substat_names, stat_rolls=GameData.substat_rolls, char_data=Character.data, echo_score="Your scores will be displayed here", 
                               echo_tier="Your tiers will be shown here", prev_char="Carlotta", prev_er="100", prev_buff="None")
    elif request.method == "POST":
        try: 
            es, et = main(request.form["char_full"], 
                          request.form["buff_full"], 
                          request.form["er_tot_full"], 
                          [[request.form["Crit Rate(%) 1"], request.form["Crit Damage(%) 1"], request.form["Atk(%) 1"], request.form["Flat Atk 1"], request.form["HP(%) 1"], request.form["Flat HP 1"], 
                           request.form["Def(%) 1"], request.form["Flat Def 1"], request.form["Basic(%) 1"], request.form["Heavy(%) 1"], request.form["Skill(%) 1"], request.form["Liberation(%) 1"],
                           request.form["ER(%) 1"]], 
                           [request.form["Crit Rate(%) 2"], request.form["Crit Damage(%) 2"], request.form["Atk(%) 2"], request.form["Flat Atk 2"], request.form["HP(%) 2"], request.form["Flat HP 2"], 
                           request.form["Def(%) 2"], request.form["Flat Def 2"], request.form["Basic(%) 2"], request.form["Heavy(%) 2"], request.form["Skill(%) 2"], request.form["Liberation(%) 2"], 
                           request.form["ER(%) 2"]], 
                           [request.form["Crit Rate(%) 3"], request.form["Crit Damage(%) 3"], request.form["Atk(%) 3"], request.form["Flat Atk 3"], request.form["HP(%) 3"], request.form["Flat HP 3"], 
                           request.form["Def(%) 3"], request.form["Flat Def 3"], request.form["Basic(%) 3"], request.form["Heavy(%) 3"], request.form["Skill(%) 3"], request.form["Liberation(%) 3"], 
                           request.form["ER(%) 3"]], 
                           [request.form["Crit Rate(%) 4"], request.form["Crit Damage(%) 4"], request.form["Atk(%) 4"], request.form["Flat Atk 4"], request.form["HP(%) 4"], request.form["Flat HP 4"], 
                           request.form["Def(%) 4"], request.form["Flat Def 4"], request.form["Basic(%) 4"], request.form["Heavy(%) 4"], request.form["Skill(%) 4"], request.form["Liberation(%) 4"], 
                           request.form["ER(%) 4"]], 
                           [request.form["Crit Rate(%) 5"], request.form["Crit Damage(%) 5"], request.form["Atk(%) 5"], request.form["Flat Atk 5"], request.form["HP(%) 5"], request.form["Flat HP 5"], 
                           request.form["Def(%) 5"], request.form["Flat Def 5"], request.form["Basic(%) 5"], request.form["Heavy(%) 5"], request.form["Skill(%) 5"], request.form["Liberation(%) 5"], 
                           request.form["ER(%) 5"]]], 
                           "full")
            return render_template("full.html", stat_names=GameData.substat_names, stat_rolls=GameData.substat_rolls, char_data=Character.data, echo_score=es, echo_tier=et, 
                                   prev_char=request.form["char_full"], prev_er=request.form["er_tot_full"], prev_buff=request.form["buff_full"])
        except Exception as msg: return f"<h1>Error 69_420: </h1><br><h2>{msg}</h2><br><p>Site is under contruction and not yet fully complete. Forwarding the above error name to me ('AstyuteChick' at Reddit and GitHub) would be of great help!</p>"
    else: raise ValueError

@evc_app.route("/instruct")
def instruct():
    return render_template("instruct.html")

@evc_app.route("/logs")
def logs():
    return render_template("logs.html")

if __name__ == "__main__": evc_app.run(debug=True)
