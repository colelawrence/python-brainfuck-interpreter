-                       Start with minus 1
>+
,                       Read input and print if input is enter key
----- ----- ---         Check if enter key 13
[
  +++++ +++++ +++     Reset
  [                   a 0 0
    >+
    >+
    <<-
  ]                   0 a a
                      ^
  >>
  [                   0 a a
    <<+
    >>-
  ]                   a a 0
  <
                      a a 0
                        ^
  ,                 If not enter then input
  ----- ----- ---   Check if enter key 13
]
-                       Mark last cell with minus 1
<+                      Start moving backwards
[
  -
  <+                    Until we get to first cell which equals minus 1
]
>+                      Start moving forwards
[
  -
  [
    .                 Print if character
    [-]               Reset current character
  ]
  >+                  Until we get to last cell which we set to minus 1
]