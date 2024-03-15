import customtkinter
import os

from tkinter import *
from tkinter import filedialog

from find_duplicates import generate_duplicates
from find_unique import generate_unique
from copy_files import copy_files_from_csv

GEOMETRY_X = 500 #probably not necessary but easy to change the window dimension here
GEOMETRY_Y = 320
sidebar_width = int(GEOMETRY_X * 0.14)
main_frame_width = GEOMETRY_X - sidebar_width


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk() #configure the root frame for customtkinter
root.title("PYFile Image Manager")
root.geometry(f"{GEOMETRY_X}x{GEOMETRY_Y}")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


def menu_frame(): #configure the left menu bar frame

    sidebar_frame = customtkinter.CTkFrame(root, 
        width=sidebar_width, 
        height=GEOMETRY_Y, 
        corner_radius=0, 
        fg_color="#303030"
        )
    
    sidebar_frame.grid(row=0, 
        column=0, 
        sticky="nsw"
        )

    sidebar_label = customtkinter.CTkLabel(sidebar_frame, 
        text="Manage Images", 
        font=customtkinter.CTkFont(size=20, weight="bold")
        )
    
    sidebar_label.grid(row=0, 
        column=0, 
        padx=20, 
        pady=(20, 10)
        )
    
    sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, 
        text="Generate File Listing", 
        command=generate_files_frame
        )

    sidebar_button_1.grid(row=1, 
        column=0, 
        padx=20, 
        pady=10
        )

    sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, 
        text="Copy Files", 
        command=copy_files_frame
        )

    sidebar_button_3.grid(row=3, 
        column=0, 
        padx=20, 
        pady=10
        )

    sidebar_button_4 = customtkinter.CTkButton(sidebar_frame, 
        text="Delete Files", 
        command=delete_files_frame
        )

    sidebar_button_4.grid(row=4, 
        column=0, 
        padx=20, 
        pady=10
        )

    sidebar_button_5 = customtkinter.CTkButton(sidebar_frame, 
        text="Return Home", 
        command=home_frame
        )

    sidebar_button_5.grid(row=5, 
        column=0, 
        padx=20, 
        pady=10
        )


def home_frame(): #define the home frame which is the one displayed when first launched.

    main_frame = customtkinter.CTkFrame(root, 
        width=main_frame_width, 
        corner_radius=0, 
        fg_color="#404040"
        )
    
    main_frame.grid(row=0, 
        column=1, 
        sticky="nsew"
        )
         
    main_label = customtkinter.CTkLabel(main_frame, 
        text="Select option from menu", 
        font=customtkinter.CTkFont(size=20, weight="bold")
        )
    
    main_label.grid(row=0, 
        column=0, 
        padx=20, 
        pady=(20, 10)
        )
    

def generate_files_frame(): #define the frame appearance when requesting Generate Duplicate List
    
    global path_name

    main_frame = customtkinter.CTkFrame(root,
        width=main_frame_width, 
        corner_radius=0, 
        fg_color="#404040"
        )
    
    main_frame.grid(row=0, 
        column=1, 
        sticky="nsew"
        )
    
    main_label = customtkinter.CTkLabel(main_frame, 
        text="Create File List", 
        font=customtkinter.CTkFont(size=20, weight="bold")
        )
    
    main_label.grid(row=0, 
        column=0, 
        padx=20, 
        pady=(20, 10), 
        sticky="nsw"
        )
    
    selectFolderPath_button = customtkinter.CTkButton(main_frame, 
        text="Select a Folder Path", 
        command=select_folder
        )
    
    selectFolderPath_button.grid(row=2, 
        column=0, 
        padx=20, 
        pady=10,
        sticky="w"
        )
    
    selectGenerateList_button = customtkinter.CTkButton(main_frame, 
        text="Generate Lists", 
        command=generate_lists_clicked
        )
    
    selectGenerateList_button.grid(row=3, 
        column=0, 
        padx=20, 
        pady=10,
        sticky="w"
        )
    
    selectOpenList_button = customtkinter.CTkButton(main_frame, 
        text="Open", 
        command=open_the_csv
        )
    
    selectOpenList_button.grid(row=4, 
        column=0, 
        padx=20, 
        pady=10,
        sticky="w"
        )


def copy_files_frame(): #define the main frame when a list is generated and the copy process is to be enacted

    main_frame = customtkinter.CTkFrame(root, 
        width=main_frame_width, 
        corner_radius=0, 
        fg_color="#404040"
        )
    
    main_frame.grid(row=0, 
        column=1, 
        sticky="nsew"
        )
    
    main_label = customtkinter.CTkLabel(main_frame, 
        text="Copy Files", 
        font=customtkinter.CTkFont(size=20, weight="bold")
        )
    
    main_label.grid(row=0, 
        column=0, 
        padx=20, 
        pady=(20, 10)
        )
    
    selectFolderPath_button = customtkinter.CTkButton(main_frame, 
        text="Select Source csv", 
        command=select_source_csv
        )
    
    selectFolderPath_button.grid(row=2, 
        column=0, 
        padx=20, 
        pady=10,
        sticky="w"
        )
    
    selectGenerateList_button = customtkinter.CTkButton(main_frame, 
        text="Select Destination Path", 
        command=select_destination_path
        )
    
    selectGenerateList_button.grid(row=3, 
        column=0, 
        padx=20, 
        pady=10,
        sticky="w"
        )
    
    selectOpenList_button = customtkinter.CTkButton(main_frame, 
        text="Start Copying", 
        command=start_copying
        )
    
    selectOpenList_button.grid(row=4, 
        column=0, 
        padx=20, 
        pady=10,
        sticky="w"
        )


def delete_files_frame(): #define the main frame when the intent is to bulk delete files from a list (usually delete duplicates)

    main_frame = customtkinter.CTkFrame(root, 
        width=main_frame_width, 
        corner_radius=0, 
        fg_color="#404040"
        )
    
    main_frame.grid(row=0, 
        column=1, 
        sticky="nsew"
        )

    main_label = customtkinter.CTkLabel(main_frame, 
        text="This frame will provide\nfunctionality for the deleting\nfiles function", 
        font=customtkinter.CTkFont(size=20, weight="bold")
        )
    
    main_label.grid(row=0, 
        column=0, 
        padx=20, 
        pady=20,
        sticky="w"
        )


def select_folder(): #select the folder to create the list of duplicate and unique files
    global path_name
    path_name = filedialog.askdirectory(initialdir="/", 
        title="Select a Folder"
        )
    print(path_name, "was selected as the path for analysis")


def generate_lists_clicked():
    print("Searching for duplicates in", path_name)
    generate_duplicates(path_name)
    print("Searching for unique files in", path_name)
    generate_unique(path_name)
    #refer https://stackoverflow.com/questions/77383219/how-do-i-make-a-customtkinter-button-run-a-function-without-freezing for big directory may need to thread


def open_the_csv():
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "Duplicates.csv")) != 0:
        os.startfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "Duplicates.csv"))
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "UniqueFiles.csv")) != 0:
        os.startfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "UniqueFiles.csv"))


def select_source_csv(): #for copying or deleting the csv contents
    global source_name
    source_name = filedialog.askopenfilename(initialdir=os.path.join(os.path.dirname((os.path.abspath(__file__))), "Output"),
        title="Select Duplicates or UniqueFiles csv File"
        ) 
    print(source_name, "was selected as the source csv")   


def select_destination_path(): #for copying the csv contents to
    global destination_name
    destination_name = filedialog.askdirectory(initialdir="/", 
        title="Select a destination Folder"
        ) 
    print(destination_name, "was selected as the destination folder")


def start_copying():
    print("Copying commenced")
    copy_files_from_csv(source_name, destination_name)


#placeholders for actions invoked by pressing a button
def delete_files_clicked():
    pass


home_frame() #create the home frame when starting main.py
menu_frame() #create the menu sidebar too
root.mainloop() #go time
