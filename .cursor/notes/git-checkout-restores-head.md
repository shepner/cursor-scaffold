# `git checkout -- file` restores HEAD, not your edit

Parent:: [Learn from mistakes](learn-from-mistakes.md)

`git checkout -- path` means "make this path match the index / HEAD", not
"undo the last mutation I made".

On an **uncommitted** file that already carried other edits, those go with it.
A negative control that mutates the real file and then checkouts it back is how
those other edits vanish.

**Do this instead.** Mutate a **copy** (`cp file /tmp/file.mut` and run the
check on the copy), or commit first so HEAD already has the real change.

agent-commons `soas1huu`.
