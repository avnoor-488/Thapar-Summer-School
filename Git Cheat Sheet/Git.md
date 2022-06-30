
# Git Cheat Sheet

Git is a distributed version control system that helps developers collaborate on projects of any scale.



## Setup your Git username:
With the command below you can configure your user name:

```bash
  git config --global user.name "avnoor-488"
```



## Setup your Git user email:
This command lets you setup the user email address you'll use in your commits.

```bash
git config --global user.email "avnoorsingh488@gmail.com"
```
## Initialize a Empty Git repo:
Everything starts from here. The first step is to initialize a new Git repo locally in your project root. You can do so with the command below:

```bash
git init
```
## Add a file to the staging area in Git:

The command below will add a file to the current directory. Just replace "filename_here"  with the name of the file you want to add to the directory.
```bash
git add filename_here
```
Or if you want to add all the files present in the directory not just a single file, then the command is:
```bash
git add .
```


## Check a repository's status in Git:
This command will show the status of the current repository including staged, unstaged, and untracked files.

```bash
git status
```
## Commit changes in the editor in Git:

This command will open a text editor in the terminal where you can write a full commit message.

A commit message is made up of a short summary of changes, an empty line, and a full description of the changes after it.

```bash
git commit -m "message you want to send with commit"
```
## See your commit history in Git:
This command shows the commit history for the current repository:

```bash
git log
```
And  to see your commit history including changes in Git,

```bash 
git log -p
```
## To see a specific commit in Git:

This command shows a specific commit.
Every commit comes with it's own unique commit-id.
Replace commit-id with the id of the commit that you find in the commit log after the word commit.

```
git show commit-id
```
## See changes made before committing them using "diff" in Git:

You can pass a file as a parameter to only see changes on a specific file.
git diff shows only unstaged changes by default.

We can call diff with the --staged flag to see any staged changes.

```
git diff
git diff all_checks.py
git diff --staged
```
## Revert unstaged changes in Git
```
git checkout filename
```
## To create a new branch in Git:
By default, you have one branch, the main branch. With this command, you can create a new branch. Git won't switch to it automatically – you will need to do it manually with the next command.
```
git branch branch_name

```

##  To switch to a newly created branch in Git:
When you want to use a different or a newly created branch you can use this command: 
```
git checkout branch_name

```

## To list branches in Git:

You can view all created branches using the git branch command. It will show a list of all branches and mark the current branch with an asterisk and highlight it in green.

```
git branch
```


## To create a branch in Git and switch to it immediately:
```
git checkout -b branch_name
```
##  To delete a branch in Git:
As soon as you are done working with a branch and have merged it, you can delete it using the command below:

```
git branch -d branch_name
```
## To merge two branches in Git:
To merge the history of the branch you are currently in with the branch_name, you will need to use the command below:

```
git merge branch_name
```
## To abort a conflicting merge in Git:
If you want to throw a merge away and start over, you can run the following command:

```
git merge --abort

```

## To add a remote repository in Git:
This command adds a remote repository to your local repository (just replace https://repo_here with your remote repo URL).

```
git add remote https://repo_here
```
## To get more info about a remote repo in Git:
Just replace origin with the name of the remote obtained by
running the git remote -v command.
```
git remote show origin
```
##  Push changes to a remote repo in Git:
When all your work is ready to be saved on a remote repository, you can push all changes using the command below:

```
git push

```
##  Pull changes from a remote repo in Git:
If other team members are working on your repository, you can retrieve the latest changes made to the remote repository with the command below:
It is always recommended that, before pushing something into repo always take a pull from origin.
```
git pull
```
## Push a new branch to a remote repo in Git:
If you want to push a branch to a remote repository you can use the command below. Just remember to add -u to create the branch upstream:

```
git push -u origin branch_name
```

## Force a push request in Git:
This command will force a push request. This is usually fine for pull request branches because nobody else should have cloned them.
But this isn't something that you want to do with public repos.
```
git push -f
```

# References
-> https://www.codewithharry.com

-> https://wwww.codewithmosh.com

#### P.S : You don't need to remember all these commands always, use this cheat sheet to ease yourself and just keep practising the stuff for better understanding.
