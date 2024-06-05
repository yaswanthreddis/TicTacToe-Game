import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("TicTacToe")
        self.buttonsGrid=[]
        
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=14,height=7,background="cyan",command=lambda i=i,j=j:self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttonsGrid.append(row)
            
            
    def make_move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col] =self.current_player
            self.buttonsGrid[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over","The Winner is :"+self.current_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo("Game Over"," It's draw")
                self.window.quit()
            self.current_player = "O" if self.current_player=="X" else "X"
    
    def check_winner(self,player):
        for i in range(3):
            #Condition For Checking Rows
            if player==self.board[i][0]==self.board[i][1]==self.board[i][2]:
                return True
            #Condition For Checking Rows
            if player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
                return True
        if player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
                return True    
        if player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
                return True   
        return False
    
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    
    def run(self):
        self.window.mainloop()


game= TicTacToe()
game.run()

        
        