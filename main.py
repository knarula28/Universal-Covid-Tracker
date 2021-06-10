from tkinter import *
import tkinter as tk 
from covid import Covid
#from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font


covid = Covid()

def popupscreen():
    def countrystatus():
        countryinput =ctname.get()
        if countryinput == '': # we should add error if its invalid country too
            return messagebox.showerror('Error','Invalid country name')
            # fix this because error box isnt popping up 
        
        else:
            covidstats =covid.get_status_by_country_name(countryinput)
            countrystats =Toplevel() # this puts this screen ontop of other screen 
            countrystats.geometry('300x300')
            countrystats.configure(background = '#000000')
            countrystats.resizable(width = False, height = False)
            
            # countrystats.resizable(width = False, height = False)co
            countrystats.title(countryinput + "'s" + " current COVID status")

            status_label = tk.Label(countrystats, text = 'Status:', font = 'Helvetica 22 bold', background = '#000000',foreground="#FFFFFF")
            status_label.grid(row=1, ipadx = 100)
            
            confirmed_label= tk.Label(countrystats,text='Confirmed cases: '+str(covidstats['confirmed']), font = 'Helvetica 14 bold', background = '#000000',foreground="#FFFFFF")
            confirmed_label.grid(row=2, sticky = W)
            
            active_label = tk.Label(countrystats,text='Active cases: '+str(covidstats['active']), font = 'Helvetica 14 bold', background = '#000000',foreground="#FFFFFF")
            active_label.grid(row=3, sticky = W), 
            
            death_label = tk.Label(countrystats,text='Deaths: '+str(covidstats['deaths']), font = 'Helvetica 14 bold', background = '#000000',foreground="#FFFFFF")
            death_label.grid(row=4,sticky = W)
            
            recoveries_label = tk.Label(countrystats,text='Recoveries: '+str(covidstats['recovered']), font = 'Helvetica 14 bold', background = '#000000',foreground="#FFFFFF")
            recoveries_label.grid(row=5,sticky = W)
         
            popupbox.destroy()

    ctname=StringVar()
    popupbox=Toplevel()
    popupbox.configure(background = '#000000')
    popupbox.geometry('400x100')
    popupbox.resizable(width = False, height = False)
    
    country_label = tk.Label(popupbox,text='Enter country name:',background = '#000000',foreground="#FFFFFF")
    country_label.grid(row=2,column=1, ipady = 30)
    Entry(popupbox,width=15,textvariable=ctname).grid(row=2,column=2)
    
    search_button = tk.Button(popupbox,text='Search',font = 'Helvetica 14 bold',fg = '#C61C1C',bg = '#FFFFFF',bd =  10,relief = "raised", highlightthickness=3, highlightcolor="#FFFFFF", highlightbackground="#FABDE8",borderwidth=4, command=countrystatus)
    search_button.grid(row=2,column=3)
        


# main screen

mainscreen = tk.Tk()
mainscreen.title("Universal Covid-19 Tracker")
mainscreen.configure(background = '#000000')
mainscreen.geometry("600x280")
mainscreen.resizable(width = False, height = False)
titlefont = Font(family = "Helvetica", size = 28, weight = "bold", underline = 1)


main_label = tk.Label(mainscreen, text = "Latest Updates on Covid-19", background = '#000000',foreground="#FFFFFF", font = titlefont )
main_label.grid(row = 0, ipadx = 100)
                      


total_cases = tk.Label(mainscreen, text = "Total Confirmed Cases: " +str(covid.get_total_confirmed_cases()),background = '#000000',foreground="#FFFFFF", font = 'Helvetica 14 ')
total_cases.grid(row = 2, sticky = W, ipady = 10)


total_active_cases = tk.Label(mainscreen, text = "Total Active Cases: " + str(covid.get_total_active_cases()), background = '#000000',foreground="#FFFFFF", font = 'Helvetica 14')
total_active_cases.grid(row = 3, sticky = W, ipady = 10)

total_deaths = tk.Label(mainscreen, text = "Total Deaths: " + str(covid.get_total_deaths()), background = '#000000',foreground="#FFFFFF", font = 'Helvetica 14')
total_deaths.grid(row = 4, sticky = W, ipady = 10)

# creating button



main_button = tk.Button(mainscreen, text = "Click for Cases by Country",font = 'Helvetica 14 bold',fg = '#C61C1C',bg = '#FFFFFF',bd =  10,relief = "raised", highlightthickness=3, highlightcolor="#FFFFFF", highlightbackground="#FABDE8",borderwidth=4, command = popupscreen)
main_button.grid(row = 7, padx = 100, pady = 20)

        
mainscreen.mainloop()
