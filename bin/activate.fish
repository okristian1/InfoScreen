<<<<<<< HEAD
# This file must be used with ". bin/activate.fish" *from fish* (http://fishshell.org)
# you cannot run it directly

function deactivate  -d "Exit virtualenv and return to normal shell environment"
=======
# This file must be used using `. bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
>>>>>>> 47aae85e66156039fe4ab4775101fc4fa9e8376b
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
<<<<<<< HEAD
=======

>>>>>>> 47aae85e66156039fe4ab4775101fc4fa9e8376b
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
<<<<<<< HEAD
        functions -e fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
        . ( begin
                printf "function fish_prompt\n\t#"
                functions _old_fish_prompt
            end | psub )
        functions -e _old_fish_prompt
    end

    set -e VIRTUAL_ENV
    if test "$argv[1]" != "nondestructive"
        # Self destruct!
=======
        # Set an empty local `$fish_function_path` to allow the removal of `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
    end

    set -e VIRTUAL_ENV

    if test "$argv[1]" != 'nondestructive'
        # Self-destruct!
        functions -e pydoc
>>>>>>> 47aae85e66156039fe4ab4775101fc4fa9e8376b
        functions -e deactivate
    end
end

<<<<<<< HEAD
# unset irrelavent variables
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/locrin/Documents/infoskjerm"
=======
# Unset irrelevant variables.
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/locrin/projects/project1/flask"
>>>>>>> 47aae85e66156039fe4ab4775101fc4fa9e8376b

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

<<<<<<< HEAD
# unset PYTHONHOME if set
=======
# Unset `$PYTHONHOME` if set.
>>>>>>> 47aae85e66156039fe4ab4775101fc4fa9e8376b
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

<<<<<<< HEAD
if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.

    # save the current fish_prompt function as the function _old_fish_prompt
    . ( begin
            printf "function _old_fish_prompt\n\t#"
            functions fish_prompt
        end | psub )

    # with the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Prompt override?
        if test -n "(infoskjerm) "
            printf "%s%s%s" "(infoskjerm) " (set_color normal) (_old_fish_prompt)
            return
        end
        # ...Otherwise, prepend env
        set -l _checkbase (basename "$VIRTUAL_ENV")
        if test $_checkbase = "__"
            # special case for Aspen magic directories
            # see http://www.zetadev.com/software/aspen/
            printf "%s[%s]%s %s" (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal) (_old_fish_prompt)
        else
            printf "%s(%s)%s%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal) (_old_fish_prompt)
        end
=======
function pydoc
    python -m pydoc $argv
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
        # Save the current $status, for fish_prompts that display it.
        set -l old_status $status

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ""
            printf '%s%s' "" (set_color normal)
        else
            printf '%s(%s%s%s) ' (set_color normal) (set_color -o white) (basename "$VIRTUAL_ENV") (set_color normal)
        end

        # Restore the original $status
        echo "exit $old_status" | source
        _old_fish_prompt
>>>>>>> 47aae85e66156039fe4ab4775101fc4fa9e8376b
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end
