# hackohio-veeva
Veeva challange for Hack OHI/O

# How to use git???
Git is complicated as shit, but as long as you follow the basic procedure and don't mess up, you should be fine. The basic idea:
- You "pull" updates from the repository to your local copy.
- Make changes to your local copy.
- Tell git which changed files you want to "commit".
- Commit your changes locally.
- Rinse and repeat until you're done with your changes, and then "push" your local commits back onto the main repository.

The basic commands are:

- git pull - Pulls the repository to your local copy.
- git status - Tells you the status of your local repository.
    - Red files are untracked. Ignore the files listed under "Untracked Files", those are supposed to be untracked.
- git add <filename> - Tells git to start tracking a file.
- git commit - Commits the changes in your tracked files. It should open a text editor where you will write a description of the commit. Save and close, and the commit should finish.
- git push - Pushes your commits to the main repository.

Sometimes, a file has multiple changes which needs to be merged before they can be pushed. I'll add more detail to this later, but the general idea is you'll need to open the file, find where the changes are (they'll be marked with something like "======>" at the top and some weird numbers at the bottom). It's up to you how to combine the changes. Once you're done, recommit and push.

And finally, always remember: Always pull before you push!