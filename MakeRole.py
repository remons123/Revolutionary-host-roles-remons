# coding: shift_jis
from tkinter import Text
from turtle import color


while True:
     RHR = "RevolutionaryHostRoles\\"

     #��E�����
     RoleName = input("�p��̖�E�� : ")
     JapaneseRoleName = input("���{��̖�E�� : ")
     Team = input("�w�c(�N���[or�C���|�X�^�[) : ")
     Color = input("�F(red = ��, blue= ��, yellow = ���F�ȂǏ�����and�p��) : ")
     UseVent = input("�x���g�g�p�\��(�g�p�\�ȏꍇ�L�����Ȃ��Ă����v�ł��A�g�p�s�̏ꍇfalse�Ə����Ă�������) : ")
     UseSabotage = input("�T�{�^�[�W���g�p�\��(�g�p�\�ȏꍇ�L�����Ȃ��Ă����v�ł��A�g�p�s�̏ꍇfalse�Ə����Ă�������) : ")
     OptionId = input("�I�v�V������Id : ")
#���f
     if "false" in UseVent:
         CanUseVent = False
     else:
         CanUseVent = True
     if "false" in UseSabotage:
         CanUseSabotage = False
     else:
         CanUseSabotage = True

#�\�[�X�R�[�h��������

     #RoleAssifnment��������
     with open(RHR + "Patches\\RoleAssignment.cs", "r", encoding="utf-8") as RAR:
          RA2 = RAR.read()

          if Team == "�N���[":
             TeamText = "crew"
          elif Team == "�C���|�X�^�[":
               TeamText = "imp"
          else:
              print("�w�c���u�N���[�v�܂��́u�C���|�X�^�[�v�ł͂���܂���B")
              exit()

          with open(RHR + "Patches\\RoleAssignment.cs", "w", encoding="utf-8") as RAW:
               text = RA2.replace(f"//{Team}", f"""{TeamText}Settings.Add((byte)CustomRoleId.{RoleName}, CustomOptionHolder.{RoleName}Option.GetSelection());\n            //{Team}""")
               RAW.write(text)
    #RoleId��������
     with open(RHR + "Roles\\RoleOption\\RoleId.cs", "r", encoding="utf-8") as RoleIdR:
          RoleIdR2 = RoleIdR.read()
          with open(RHR + "Roles\\RoleOption\\RoleId.cs", "w", encoding="utf-8") as RoleIdW:
               RoleIdtext = RoleIdR2.replace(f"//�Ȃ�ł���E", f"""{RoleName},\n        //�Ȃ�ł���E""")
               RoleIdW.write(RoleIdtext)
    #RoleDatas
     with open(RHR + "Roles\\RoleOption\\RoleDatas.cs", "r", encoding="utf-8") as RoleDatasR:
          RoleDatasR2 = RoleDatasR.read()
          with open(RHR + "Roles\\RoleOption\\RoleDatas.cs", "w", encoding="utf-8") as RoleDatasW:
               RoleDatastext = RoleDatasR2.replace(f"//RoleDatas", "        public static class {RoleName}\n         {\n            public static Color color = Color.{playercolor};\n            public static List<PlayerControl> {RoleName}Player;\n            public static void DataLoad()\n            {\n                {RoleName}Player = new();\n            }\n        }\n//RoleDatas").replace("{RoleName}", RoleName).replace("{playercolor}", Color)
               RoleDatasW.write(RoleDatastext)
    #RoleDatas
     with open(RHR + "Roles\\RoleOption\\RoleDatas.cs", "r", encoding="utf-8") as RoleDataR:
          RoleDataR2 = RoleDataR.read()
          with open(RHR + "Roles\\RoleOption\\RoleDatas.cs", "w", encoding="utf-8") as RoleDataW:
               RoleDatatext = RoleDataR2.replace(f"//DataLoad���悤",f"{RoleName}.DataLoad();\n            //DataLoad���悤")
               RoleDataW.write(RoleDatatext)
     #CustomRPC          
     with open(RHR + "Patches\\CustomRPC.cs", "r", encoding="utf-8") as CustomRPCR:
          CustomRPCR2 = CustomRPCR.read()
          with open(RHR + "Patches\\CustomRPC.cs", "w", encoding="utf-8") as CustomRPCW:
               CustomRPCtext = CustomRPCR2.replace("//Role������", f"case CustomRoleId.{RoleName}:\n                            RoleDatas.{RoleName}.{RoleName}Player.Add(player);\n                            break;\n                        //Role������")
               CustomRPCW.write(CustomRPCtext)
    #Helper
     with open(RHR + "Helper.cs", "r", encoding="utf-8") as HelpersR:
          HelpersR2 = HelpersR.read()
          with open(RHR + "Helper.cs", "w", encoding="utf-8") as HelpersW:
               Helperstext = HelpersR2.replace(f"//MOD�̖�E",f"else if (RoleDatas.{RoleName}.{RoleName}Player.IsCheckListPlayerControl(p)) return CustomRoleId.{RoleName};\n            //MOD�̖�E")
               HelpersW.write(Helperstext)
     with open(RHR + "Helper.cs", "r", encoding="utf-8") as HelperR:
          HelperR2 = HelperR.read()
          with open(RHR + "Helper.cs", "w", encoding="utf-8") as HelperW:
               HelperNametext = HelperR2.replace("//RoleNameText", f"""case CustomRoleId.{RoleName}:\n                    return Helpers.cs(Color.{Color}, "{JapaneseRoleName}");\n                //RoleNameText""")
               HelperW.write(HelperNametext)
     #CustomOption
     with open(RHR + "Patches\\GameOptions\\CustomOptionHolder.cs", "r", encoding="utf-8") as CustomOptionHolderR:
          CustomOptionHolderR2 = CustomOptionHolderR.read()
          with open(RHR + "Patches\\GameOptions\\CustomOptionHolder.cs", "w", encoding="utf-8") as CustomOptionHolderW:
               CustomOptionHoldertext = CustomOptionHolderR2.replace(f"//CustomOptionHolder3�ł�", f"public static CustomOption {RoleName}Option;\n\n        //CustomOptionHolder3�ł�")
               CustomOptionHolderW.write(CustomOptionHoldertext)
     with open(RHR + "Patches\\GameOptions\\CustomOptionHolder.cs", "r", encoding="utf-8") as CustomOptionHoldersR:
          CustomOptionHoldersR2 = CustomOptionHoldersR.read()
          with open(RHR + "Patches\\GameOptions\\CustomOptionHolder.cs", "w", encoding="utf-8") as CustomOptionHoldersW:
               if Team == "�N���[":
                  TeamTexts = "Crewmate"
                  TeamText2 = "Crew"
               elif Team == "�C���|�X�^�[":
                    TeamTexts = "Impostor"
                    TeamText2 = "Impo"
               CustomOptionHoldertext2 = CustomOptionHoldersR2.replace(f"//CustomOptionHolder2�ł�", f"""{RoleName}Option = CustomOption.Create({TeamText2} + {OptionId}, Types.{TeamTexts}, cs(Color.{Color}, "{JapaneseRoleName}"), rates, null, true);\n\n            //CustomOptionHolder2�ł�""")
               CustomOptionHoldersW.write(CustomOptionHoldertext2)
    #PlayerControl�T�{�^�[�W���s��E
     with open(RHR + "Patches\\PlayState\\PlayerControl\\PlayerControl.cs", "r", encoding="utf-8") as PCsR:
          PCsR2 = PCsR.read()
          with open(RHR + "Patches\\PlayState\\PlayerControl\\PlayerControl.cs", "w", encoding="utf-8") as PCsW:
               if not CanUseSabotage:
                  PCstext = PCsR2.replace(f"//�T�{�^�[�W���s��E", f"case CustomRoleId.{RoleName}:\n                //�T�{�^�[�W���s��E")
               else:
                    PCstext = PCsR2.replace(f"//�T�{hohifhwfhwifhawihgihwpghaiguhargihearigearpihgeaiphgaiuhgbavfhiuhfiw�^�[�W���s��E", f"case CustomRoleId.{RoleName}\n                //�T�{�^�[�W���s��E")
               PCsW.write(PCstext)
               #�x���g
     with open(RHR + "Patches\\PlayState\\PlayerControl\\PlayerControl.cs", "r", encoding="utf-8") as PCR:
          PCR2 = PCR.read()
          with open(RHR + "Patches\\PlayState\\PlayerControl\\PlayerControl.cs", "w", encoding="utf-8") as PCW:
               if not CanUseVent:
                                     PCtext = PCR2.replace(f"//�x���g�s��E", f"case CustomRoleId.{RoleName}:\n                //�x���g�s��E")
               else:
                                     PCtext = PCR2.replace(f"//�T�{�^�[�Wfawaweghwjsyeturyhregwfyhrtegsafght���s��E", f"case CustomRoleId.{RoleName}\n                //�T�{�^�[�W���s��E")
               PCW.write(PCtext)
    #MakeText
     print("�쐬�ł������������������I�I�I")