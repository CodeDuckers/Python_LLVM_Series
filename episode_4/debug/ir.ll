; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
main_entry:
  %".2" = mul i32 5, 3
  %".3" = sub i32 %".2", 2
  ret i32 %".3"
}
