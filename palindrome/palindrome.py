from rich import print

doYouWantToResume = True

while doYouWantToResume:
    userWord = input("Please enter a word to see if it is palindrome: ")
    wordInReverse = userWord[::-1]
    
    if userWord == wordInReverse:
        print(f"[bold green]Your word was '{userWord}' and when you reverse it, it is still '{wordInReverse}'.[/bold green]")
        print("[bold green]Your word is a palindrome.[/bold green]\n")
    else:
        print(f"[bold red]Your word was '{userWord}' and when you reverse it, it becomes '{wordInReverse}'.[/bold red]")
        print("[bold red]Your word isn't a palindrome.[/bold red]\n")
    
    resumeWord = input("Do you want to enter another word? (yes/no): ").lower()
    if resumeWord == "yes":
        continue
    elif resumeWord == "no":
        doYouWantToResume = False
    else:
        print("[bold magenta]Please enter a valid response (yes or no).[/bold magenta]\n")
