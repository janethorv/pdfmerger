import tkinter as tk
from tkinter import Label, filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from pdfmerger import merge_pdfs

def main():
    #Creating root window
    root = tk.Tk()
    root.title('PDF-merger')
    root.resizable(False, False)
    root.geometry('600x400')

    #Creating label for filebox
    filebox_label = Label(root, text="Selected PDF-files:")

    #Creating filebox for selected PDFs to be merged
    filebox = tk.Listbox(root)
    filebox.configure(background='white', foreground='black', width=30, height=30)

    #Creating entry for chosen directory where merged PDF-file will be saved
    wpentry = tk.Entry(root)
    wpentry.configure(background='white', foreground='black')

    #Initializing empty list - will contain selected PDFs to be merged
    selected = []

    writepath = ""

    #Select files from OS filesystem via Tkinters filedialog, check if files are already selected, add non-duplicates to selected-list 
    def select_files():
    
        filenames = list(fd.askopenfilenames(title='Select files', initialdir='/', filetypes=[('pdf files', '*.pdf')]))
        
        duplicates = []
        
        #Check for selected files for duplicates, if non-duplicate: add to selected-list
        for filename in filenames:
            if filename in selected:
                duplicates.append(filename)
            if filename not in selected: 
                selected.append(filename)
        
        #Displays message if duplicates were found
        if len(duplicates) != 0:
            showinfo(title='These files are already selected', message=duplicates)
            
        #Update listbox    
        refresh_listbox()
        
    #Refresh listbox - used for updating listbox content after both adding and deleting files
    def refresh_listbox():
        filebox.delete(0, 'end')
        for filename in selected:
            filebox.insert('end', filename.split('/')[-1])
            
    #Removes the selected file from the listbox and the list of selected PDFs        
    def remove_selected_file():
        for file in filebox.curselection():
            selected.remove(selected[file])
        refresh_listbox()
            
    #Removes all files from the listbox and the list of selected PDFs
    def remove_all_files():
        selected.clear()
        filebox.delete(0, 'end')
        refresh_listbox() 
        
    def select_writepath():
        path = fd.askdirectory()
        wpentry.delete(0, 'end')
        wpentry.insert(0, path)
        wpentry.update()
        
    def merge():
        wp = wpentry.get()
        merge_pdfs(selected, wp)
        remove_all_files()
        
    #Opens OS file explorer - enables user to select one or several PDF-files for merging        
    open_files = ttk.Button(
        root,
        text='Select files',
        command=select_files
    )

    #Opens OS file explorer - enables user to select folder where merged PDF-file is saved 
    open_path = ttk.Button(
        root,
        text='Select folder',
        command=select_writepath
    )

    #Activates remove_selected_file()
    remove_selected_button = ttk.Button(
        root,
        text='Remove selected file',
        command=remove_selected_file
    )

    #Activates remove_all_files()
    remove_all_button = ttk.Button(
        root,
        text='Remove all files',
        command=remove_all_files
    )

    merge_button = ttk.Button(
        root,
        text='Merge',
        command=merge
    )


    filebox_label.pack(side='top', anchor='nw', padx=(20,20), pady=(5,0))
    filebox.pack(side='left', padx=(20,20), pady=(10,20))
    open_files.pack(expand=True)
    open_path.pack(expand=True)
    wpentry.pack()
    merge_button.pack()
    remove_selected_button.pack(side='left', anchor='w')
    remove_all_button.pack(side='left', anchor='w')

    root.mainloop()
    
if __name__ == '__main__':
    main() 
