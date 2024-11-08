#IMPORT OF THE MODULES
import pandas as pd
import numpy as np
import tkinter as tk #graphical interface
from tkinter import font, IntVar, Tk, Scale, Entry #graphical interface
import os #to open the excel file

#GENERAL CLASS
class Menus():

    #graphical interface
    def __init__(self):
        self.root = tk.Tk()

        #root
        self.root.title("Meal Generator")
        self.root.configure(bg="#FFFFFF")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        #dimensions of the window
        window_width = int(screen_width * 0.8)  #80% screen length
        window_height = int(screen_height * 0.8)  #80% screen height

        #size of the window
        self.root.geometry(f"{window_width}x{window_height}")

        #Create a Canvas to put the Frame in
        self.canvas = tk.Canvas(self.root, bg="#FFFFFF")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #add the Scrollbar
        #DONT SCROLL WITH THE MOUSE BUT CLICK ON THE SCROLLBAR TO MOVE THE SCREEN
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, anchor=tk.W)

        #Configure the Canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        #Create another frame inside the canvas to hold the widgets
        self.inner_frame = tk.Frame(self.canvas, bg="#FFFFFF")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        #header
        self.welcome_label = tk.Label(self.inner_frame, text="GENERATE YOUR OWN MEAL!", bg='#009E60', fg="#FFFFFF", font='Fixedsys 30')
        self.welcome_label.pack(anchor=tk.N)

        #gender
        self.label_gen = tk.Label(self.inner_frame, text="What is your gender?", font="Fixedsys 12", bg="#FFFFFF")
        self.label_gen.pack(ipady=10, padx=10,pady=10)

        self.button_gen_1 = tk.Button(self.inner_frame, text='Man', bg="#FFFFFF", command=self.man)
        myFont= font.Font(family='Fixedsys', size=16)
        self.button_gen_1['font'] = myFont
        self.button_gen_1.pack(ipady=0, padx=10,pady=5)

        self.button_gen_2 = tk.Button(self.inner_frame, text='Woman', bg="#FFFFFF", command=self.woman)
        self.button_gen_2['font'] = myFont
        self.button_gen_2.pack(ipady=0, padx=10,pady=5)

        #noon/evening
        self.q_rep = tk.Label(self.inner_frame, text="Would you like a meal for noon or the evening?", font="Fixedsys 12", bg="#FFFFFF")
        self.q_rep.pack(ipady=10, padx=10,pady=10)

        self.button_rep_1 = tk.Button(self.inner_frame, text='Noon', bg="#FFFFFF", command=self.noon)
        self.button_rep_1['font'] = myFont
        self.button_rep_1.pack(ipady=0, padx=10,pady=5)

        self.button_rep_2 = tk.Button(self.inner_frame, text='Evening', bg="#FFFFFF", command=self.evening)
        self.button_rep_2['font'] = myFont
        self.button_rep_2.pack(ipady=0, padx=10,pady=5)

        #vegetarian option
        self.label_veg = tk.Label(self.inner_frame, text="Would you like a vegetarian meal?", font="Fixedsys 12", bg="#FFFFFF")
        self.label_veg.pack(ipady=10, padx=10,pady=10)

        self.button_veg_1 = tk.Button(self.inner_frame, text='Yes', bg="#FFFFFF", command=self.vege)
        self.button_veg_1['font'] = myFont
        self.button_veg_1.pack(ipady=0, padx=10,pady=5)

        self.button_veg_2 = tk.Button(self.inner_frame, text='No', bg="#FFFFFF", command=self.nonvege)
        self.button_veg_2['font'] = myFont
        self.button_veg_2.pack(ipady=0, padx=10,pady=5)

        #age
        self.label_age = tk.Label(self.inner_frame, text="How old are you?", bg="#FFFFFF", font="Fixedsys 12")
        self.label_age.pack(ipady=10, padx=10,pady=10)

        self.age= tk.Entry(self.inner_frame)
        self.age.pack(ipady=5, padx=10,pady=5)

        #weight
        self.label_w = tk.Label(self.inner_frame, text="How much do you weigh, in kg?", bg="#FFFFFF", font="Fixedsys 12")
        self.label_w.pack(ipady=10, padx=10,pady=10)

        self.masse = tk.Entry(self.inner_frame)
        self.masse.pack(ipady=5, padx=10,pady=5)

        #height
        self.label_t = tk.Label(self.inner_frame, text="What is your height, in cm?", bg="#FFFFFF", font="Fixedsys 12")
        self.label_t.pack(ipady=10, padx=10,pady=10)

        self.taille = tk.Entry(self.inner_frame)
        self.taille.pack(ipady=5, padx=10,pady=5)

        #sport
        self.q_sport = tk.Label(self.inner_frame, text="How sporty are you on a scale of 1 (passive) to 5 (very active)?", font="Fixedsys 12", bg="#FFFFFF")
        self.q_sport.pack(ipady=10, padx=10,pady=10)

        self.sport = IntVar()
        self.sport.set(1)  # Initial value

        scale = Scale(self.inner_frame, from_=1, to=5, showvalue=True,
                      variable=self.sport, tickinterval=1, orient='h')
        scale.pack()

        #starts the general program
        self.button_play = tk.Button(self.inner_frame, text="GENERATE", fg='#009E60', bg="#FFFFFF", font="Fixedsys 20 ", command = self.principal)
        self.button_play.pack(ipady=20, padx=10,pady=10)

        self.need_calo = tk.Label(self.inner_frame, text=f"You need X calories", fg="#FFFFFF", font='Fixedsys 30')
        self.need_calo.pack(anchor=tk.N)

        #quit Button
        self.quit_button = tk.Button(self.inner_frame, text="Quit", bg="#FFFFFF", command=self.quit_game)
        self.quit_button.pack(ipady=5, padx=10,pady=10)

        #Update the scroll to show the whole window
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def quit_game(self): #what happens when you press quit
        self.inner_frame.destroy()
        self.root.destroy()

    #different choices of the buttons : link graphical interface/program
    def man(self):
        self.sexe = 1
        self.button_gen_1.config(text="Man", fg='#009E60')
        self.button_gen_2.config(text="Woman", fg='#000000')

    def woman(self):
        self.sexe = 0
        self.button_gen_2.config(text="Woman",fg='#009E60')
        self.button_gen_1.config(text="Man", fg='#000000')

    def noon(self):
        self.midi = 0
        self.button_rep_1.config(text="Noon", fg='#009E60')
        self.button_rep_2.config(text="Evening", fg='#000000')

    def evening(self):
        self.midi = 1
        self.button_rep_2.config(text="Evening", fg='#009E60')
        self.button_rep_1.config(text="Noon", fg='#000000')

    def vege(self):
        self.vege = 0
        self.button_veg_1.config(text="Yes", fg='#009E60')
        self.button_veg_2.config(text="No", fg='#000000')

    def nonvege(self):
        self.vege = 1
        self.button_veg_2.config(text="No", fg='#009E60')
        self.button_veg_1.config(text="Yes", fg='#000000')

    def save_sport_value(self):
        value = self.sport.get()
        print("Sport value:", value)

    #computes the max calories intake for proteins, lipids and carbs (glucides) ; data found on a website
    def quantites (self, TMB):
        max_gluc = TMB*0.45 #45% of the total calories intake for the day comes from carbs
        max_lip = TMB*0.40 #40% of the total calories intake for the day comes from lipids
        max_prot = TMB*0.15 #15% of the total calories intake for the day comes from proteins
        return(max_prot, max_lip, max_gluc)


    #computations of the quantities of each micronutrient for each food
    def calcul_q (self, cal, max_prot, max_lip, max_gluc, qp_p, ql_p, qc_p, qp_v, ql_v, qc_v, qp_c, ql_c, qc_c, qp_fa, ql_fa, qc_fa, qp_fr, ql_fr, qc_fr, qp_e, ql_e, qc_e):

        #set the constraints on the quantites of the different foods
        qfa = (0.05*cal)/(qp_fa*4.18+ql_fa*9+qc_fa*4.18) #5% of the total calorie intake of the meal is oil
        qfr = (0.08*cal)/(qp_fr*4.18+ql_fr*9+qc_fr*4.18) #8% of the total calorie intake of the meal is fruit
        qe = (0.1*cal)/(qp_e*4.18+ql_e*9+qc_e*4.18) #10% of the total calorie intake of the meal is extra

        x = (max_prot/4.18)-(qp_fa*qfa)-(qp_fr*qfr)-(qp_e*qe)
        y = (max_lip/9)-(ql_fa*qfa)-(ql_fr*qfr)-(ql_e*qe)
        z = (max_gluc/4.18)-(qc_fa*qfa)-(qc_fr*qfr)-(qc_e*qe)

        a = np.array([[qp_p, qp_v, qp_c,], [ql_p, ql_v, ql_c], [qc_p, qc_v, qc_c]])
        b = np.array([x,y,z])
        (qp, qv, qc) = np.linalg.solve(a, b) #solve linear equation

        final_q = [int(qp*1000), int(qv*1000), int(qc*1000), int(qfa*1000), int(qfr*1000), int(qe*1000)]
        return final_q


    #generates all possible meals, with some constraints
    def repas_possibles(self, cal, max_prot, max_lip, max_gluc, carb,extra,fat,protein,fruit,vegetable):
        repas_possibles=[]

        for c in range(len(carb)):
            qp_c, ql_c, qc_c = carb.iloc[c,5], carb.iloc[c,6], carb.iloc[c,7] #use iloc function since the carb object is a data frame, as well as the other foods
            for e in range(len(extra)):
                qp_e, ql_e, qc_e = extra.iloc[e,5], extra.iloc[e,6], extra.iloc[e,7]
                for f in range(len(fat)):
                    qp_fa, ql_fa, qc_fa = fat.iloc[f,5], fat.iloc[f,6], fat.iloc[f,7]
                    for p in range(len(protein)):
                        qp_p, ql_p, qc_p = protein.iloc[p,5], protein.iloc[p,6], protein.iloc[p,7]
                        for fr in range(len(fruit)):
                            qp_fr, ql_fr, qc_fr = fruit.iloc[fr,5], fruit.iloc[fr,6], fruit.iloc[fr,7]
                            for v in range(len(vegetable)):
                                qp_v, ql_v, qc_v = vegetable.iloc[v,5], extra.iloc[v,6], extra.iloc[v,7]

                                final_q = self.calcul_q (cal, max_prot, max_lip, max_gluc, qp_p, ql_p, qc_p, qp_v, ql_v, qc_v, qp_c, ql_c, qc_c, qp_fa, ql_fa, qc_fa, qp_fr, ql_fr, qc_fr, qp_e, ql_e, qc_e)

                                positif = True

                                for j in final_q:
                                    if j < 0:
                                        positif = False

                                if positif: #only takes into account the meals with all positive quantities (or it makes no sense)

                                    mon_repas=[protein.iloc[p,0],vegetable.iloc[v,0],carb.iloc[c,0],fat.iloc[f,0],fruit.iloc[fr,0],extra.iloc[e,0]]
                                    chaine = "g"
                                    mon_repas2 = []

                                    for i in range(len(mon_repas)):
                                        #if it is a protein and it has a L symbol in the 2nd column
                                        if (i == 0) and protein.iloc[p,2] == "L":
                                            chaine = "mL"
                                        #if it is an oil
                                        if i == 3:
                                            chaine = "mL"
                                        #if it is an extra and it has a L symbol in the 2nd column
                                        if (i == 5) and extra.iloc[e,2] == "L":
                                            chaine = "mL"

                                        #temporary string mon_repas2, appends each new meal and is reset
                                        mon_repas2.append(final_q[i])
                                        mon_repas2.append(chaine)
                                        mon_repas2.append(mon_repas[i])
                                        chaine = "g"

                                    repas_possibles.append(mon_repas2) #repas_possibles is a list of lists of all the possible meals (considers every possibility)


        return repas_possibles


    #computation of the TMB = Metabolism Normal Rate, or the amount of calories to consume in a standard day, computed based on personnalised factors
    def calories(self):
        if self.sexe == 0:
            TMB = 655 + (9.6 * float(self.masse.get())) + (1.8 * float(self.taille.get())) - (4.7 * int(self.age.get()))
        elif self.sexe == 1:
            TMB = 66 + (13.8 * float(self.masse.get())) + (5 * float(self.taille.get())) - (6.8 * int(self.age.get()))

        #coefficients found on an internet website
        if int(self.sport.get()) == 1:
            TMB = TMB * 1.2
        elif int(self.sport.get()) == 2:
            TMB = TMB * 1.3
        elif int(self.sport.get()) == 3:
            TMB = TMB * 1.5
        elif int(self.sport.get()) == 4:
            TMB = TMB * 1.7
        elif int(self.sport.get()) == 5:
            TMB = TMB * 1.9

        if self.midi == 0:
            TMB = TMB * 0.45 #we need more calories at noon and we take breakfast into account
        elif self.midi == 1:
            TMB = TMB * 0.3 #we need less calories in the evening and we take breakfast into account

        vege = self.vege #returns wether the user is vegetarian, or not
        return TMB, vege


    #computation of the ecological score for each parameter
    def calculate_scores(self, data):
        scores = {} #scores is a new dictionnary
        for aliment, values in data.items():
            scores[aliment] = {
                "land_use_score": values[0],  #for each aliment, stores the impact of this food on this one variable
                "ghg_emissions_score": values[1],
                "acidifying_emissions_score": values[2],
                "eutrophying_emissions_score": values[3],
                "fresh_water_score" : values[4],
                "water_use_score" : values[5]
            }
        return scores

    #normalize the scores
    def normalize_scores(self, scores):
        normalized_scores = {}
        for param in ["land_use_score", "ghg_emissions_score", "acidifying_emissions_score", "eutrophying_emissions_score", "fresh_water_score", "water_use_score"]:
            max_score = max(scores[aliment][param] for aliment in scores)
            normalized_scores[param] = {aliment: scores[aliment][param] / max_score for aliment in scores}
        return normalized_scores

    #compute the global score of all the foods of the meal
    def calculate_global_score(self, normalized_scores, weights):
        global_scores = {}
        for aliment in normalized_scores["land_use_score"]:
            # computation of the global score according to the weights of the differents parameters (land use,...)
            global_scores[aliment] = sum(normalized_scores[param][aliment] * weights[param] for param in normalized_scores)
        return global_scores





        #MAIN PROGRAM
    #@profile #to compute the runtime of the program parts
    def principal(self):
        self.button_play.config(text="COMPUTING...", fg='#009E60', bg="#FFFFFF", font="Fixedsys 20") #update the display of the button GENERATE


        #NUTRITIONAL PART
        (cal, vege)=self.calories()
        print(f"Your energetic needs are {cal} kcal")

        self.need_calo.config(text=f"You need {int(cal)} kilo calories for this meal!", bg='#009E60', font='Fixedsys 30') #gives to the user its calorie recommended intake computed by the calories function
        self.inner_frame.update_idletasks() #update the tkinter modules

        #import the excel table with the amounts of proteins, glucids and lipids for each food, as a dataframe
        df = pd.read_excel("4-TableS1_augmented_with_FAO_data.xlsx", sheet_name="FAOdata")

        #creates a dataframe per foodtype
        carb = df[df["Type"].str.contains("CarbSource")]
        extra = df[df["Type"].str.contains("Extra")]
        fat = df[df["Type"].str.contains("FatSource")]
        protein0 = df[df["Type"].str.contains("ProteinSource")]
        fruit = df[df["Type"].str.contains("Fruit")]
        vegetable = df[df["Type"].str.contains("Vegetable")]


        #the vegetal protein intake contains a higher amount of carbs than animal proteins
        #not very righteous but done by hand in this case, works for this data
        protein = pd.DataFrame()

        if vege == 0:
            mask = protein0.iloc[:, 7] > 16.5 #score found "manually"
            protein = pd.concat([protein, protein0[mask]], ignore_index=True)
        else:
            protein = protein0.copy() #if the user chose "vegetarian", only the vegetal proteins are stored in the "protein" dataframe


        #we set the maximums for the amount of proteins, lipids and carbs
        (max_prot, max_lip, max_gluc) = self.quantites (cal)

        #we compute all the possible meals
        rp= self.repas_possibles(cal, max_prot, max_lip, max_gluc, carb,extra,fat,protein,fruit,vegetable)

        print(f"There are {len(rp)} possible meals", end = "\n")



        #ENVIRONMENTAL PART
        #import the excel file with the environnemental data
        df2 = pd.read_excel("5-DataS2.xlsx", sheet_name="Results - Nutritional Units")

        land_use = df2.iloc[:, 5]
        ghg = df2.iloc[:, 11]
        acidifying = df2.iloc[:, 23]
        eutrophying = df2.iloc[:, 29]
        fresh = df2.iloc[:, 35]
        stress = df2.iloc[:, 41]
        aliments = df2.iloc[:, 0]

        #initalize the dictonary to store the data on each food
        data = {}

        #loop to sort the data
        for i in range(2, len(aliments)-5):
            aliment = aliments.iloc[i]
            l = land_use.iloc[i]
            g = ghg.iloc[i]
            a = acidifying.iloc[i]
            e = eutrophying.iloc[i]
            f = fresh.iloc[i]
            s = stress.iloc[i]

            # add the data of each food to the dictionnary
            data[aliment] = (l, g, a, e, f, s)

        #weight of the parameters : we set them by increasing impact on the climate change but arbitrary values that can be changed (according to the article by J.Poore from 2018)
        #those weights depend highly on the place and conditions of production as well as the importance we choose to give a criteria
        weights = {
            "land_use_score": 0.3,
            "ghg_emissions_score": 0.4,
            "acidifying_emissions_score": 0.05,
            "eutrophying_emissions_score": 0.05,
            "fresh_water_score" : 0.1,
            "water_use_score": 0.1
        }

        #computation of the scores
        scores = self.calculate_scores(data)
        normalized_scores = self.normalize_scores(scores)
        global_scores = self.calculate_global_score(normalized_scores, weights)

        #sort the meals by increasing ecological score (the lower the score, the lower the environmental impact)
        sorted_meals = sorted(global_scores.items(), key=lambda x: x[1])


        #final sorting for the output
        final = {} #new dictionnary

        for r in range(len(rp)): #for each meal in the list of all meals
            juste_aliments = []
            facteurs = []
            for i in range(0, 16, 3):
                facteurs.append(rp[r][i]) #list of only quantities for each food
            for i in range(2, len(rp[r]), 3):
                juste_aliments.append(rp[r][i]) #list of only food name for each food

            for a in range(len(juste_aliments)):
                for c in sorted_meals:
                    if juste_aliments[a] == c:
                        facteurs[a] = facteurs[a] * sorted_meals[c] #mutliply the evironmental impact per g of food
            score_global = sum(facteurs) #all the score of each food in a meal
            final[tuple(rp[r])] = score_global #shape of the final dictionnary : tuple (easier to export as a dataframe) of a meal associated to its score


        #sort the meals by increasing score
        sorted_final = sorted(final.items(), key=lambda x: x[1])

        #display all the possible means
        data = []
        for r, score_global in sorted_final:
            meal=list(r)
            meal.append(score_global)
            data.append(meal)

        #set the columns to sort the data in a dataframe and then in an excel file
        columns = ['Quantité protéines','unité','Aliment_Prot','Quantité légume','unité','Légume','Quantité Carb','unité','Aliment_Carb','Quantité gras','unité','Aliment_Gras','Quantité fruit','unité','Fruit','Quantité extra','unité','Aliment_extra','Score Environnemental Global']
        df_repas = pd.DataFrame(data, columns=columns)
        print(df_repas.head())

        score_lettres = []

        #divides the length of number of meals by the number of letters = 5, with A = best score and E = worst score
        for i in range(len(df_repas)):
            if df_repas.iloc[i,18] not in score_lettres:
                score_lettres.append(df_repas.iloc[i,18])
        seq = int(len(score_lettres)/5)

        A = []
        B = []
        C = []
        D = []
        E = []

        #set a score to 1/5 of the meals since they are already sorted by increasing order
        for c in range(0, seq):
            A.append(score_lettres[c])
        for c in range(seq, (2*seq)):
            B.append(score_lettres[c])
        for c in range(2*seq, (3*seq)):
            C.append(score_lettres[c])
        for c in range(3*seq, (4*seq)):
            D.append(score_lettres[c])
        for c in range(4*seq, len(score_lettres)):
            E.append(score_lettres[c])

        #set the letter in the dataframe
        for s in range(len(df_repas)):
            if df_repas.iloc[s,18] in A: #the score is the 18th column
                df_repas.iloc[s,18] = 'A'
            elif df_repas.iloc[s,18] in B:
                df_repas.iloc[s,18] = 'B'
            elif df_repas.iloc[s,18] in C:
                df_repas.iloc[s,18] = 'C'
            elif df_repas.iloc[s,18] in D:
                df_repas.iloc[s,18] = 'D'
            elif df_repas.iloc[s,18] in E:
                df_repas.iloc[s,18] = 'E'


        #exports the dataframe of the meals in an excel file "repas_possibles.xlsx"
        excel_file = "repas_possibles.xlsx"
        df_repas.to_excel(excel_file, index=False)

        #change the "GENERATE" button display
        self.button_play.config(text="DONE!", fg='#009E60', bg="#FFFFFF", font="Fixedsys 20")

        #open the excel file
        os.system(f'xdg-open "{excel_file}"')


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu = Menus()
    menu.run()
