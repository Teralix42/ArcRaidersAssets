# Queen

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 23100 HP. **Internal class:** `C_Peppermint`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Queen.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Queen/01_Original_Materials_C.png"><img src="Renders/Queen/01_Original_Materials_C.png" width="48%" alt="Queen: Original Materials"></a>
<a href="Renders/Queen/03_Part_Health_C.png"><img src="Renders/Queen/03_Part_Health_C.png" width="48%" alt="Queen: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Queen/01_Original_Materials_A.png"><img src="Renders/Queen/01_Original_Materials_A.png" width="31%" alt="Queen original materials"></a>
  <a href="Renders/Queen/01_Original_Materials_B.png"><img src="Renders/Queen/01_Original_Materials_B.png" width="31%" alt="Queen original materials"></a>
  <a href="Renders/Queen/01_Original_Materials_C.png"><img src="Renders/Queen/01_Original_Materials_C.png" width="31%" alt="Queen original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Queen/02_Part_Type_A.png"><img src="Renders/Queen/02_Part_Type_A.png" width="31%" alt="Queen part type"></a>
  <a href="Renders/Queen/02_Part_Type_B.png"><img src="Renders/Queen/02_Part_Type_B.png" width="31%" alt="Queen part type"></a>
  <a href="Renders/Queen/02_Part_Type_C.png"><img src="Renders/Queen/02_Part_Type_C.png" width="31%" alt="Queen part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Queen/03_Part_Health_A.png"><img src="Renders/Queen/03_Part_Health_A.png" width="31%" alt="Queen part health"></a>
  <a href="Renders/Queen/03_Part_Health_B.png"><img src="Renders/Queen/03_Part_Health_B.png" width="31%" alt="Queen part health"></a>
  <a href="Renders/Queen/03_Part_Health_C.png"><img src="Renders/Queen/03_Part_Health_C.png" width="31%" alt="Queen part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Queen/04_Break_Off_A.png"><img src="Renders/Queen/04_Break_Off_A.png" width="31%" alt="Queen break-off parts"></a>
  <a href="Renders/Queen/04_Break_Off_B.png"><img src="Renders/Queen/04_Break_Off_B.png" width="31%" alt="Queen break-off parts"></a>
  <a href="Renders/Queen/04_Break_Off_C.png"><img src="Renders/Queen/04_Break_Off_C.png" width="31%" alt="Queen break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Queen/05_Scavenge_Interaction_A.png"><img src="Renders/Queen/05_Scavenge_Interaction_A.png" width="31%" alt="Queen scavenging"></a>
  <a href="Renders/Queen/05_Scavenge_Interaction_B.png"><img src="Renders/Queen/05_Scavenge_Interaction_B.png" width="31%" alt="Queen scavenging"></a>
  <a href="Renders/Queen/05_Scavenge_Interaction_C.png"><img src="Renders/Queen/05_Scavenge_Interaction_C.png" width="31%" alt="Queen scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Queen/06_Damage_Targets_A.png"><img src="Renders/Queen/06_Damage_Targets_A.png" width="31%" alt="Queen damage targets"></a>
  <a href="Renders/Queen/06_Damage_Targets_B.png"><img src="Renders/Queen/06_Damage_Targets_B.png" width="31%" alt="Queen damage targets"></a>
  <a href="Renders/Queen/06_Damage_Targets_C.png"><img src="Renders/Queen/06_Damage_Targets_C.png" width="31%" alt="Queen damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core_01 | 30000 | Critical | 1.5 |
| LowerLeg_01_Weakpoint_01_L_01 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_L_02 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_L_03 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_R_01 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_R_02 | 6000 | WeakPoint | 1.5 |
| LowerLeg_01_Weakpoint_01_R_03 | 6000 | WeakPoint | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Head_Laser_Socket | 30000 | — | — | 2 |
| Weapon_Launcher_Socket | 150000 | — | — | 11 |
| LowerLegGroundContact_01_L_01 | — | — | — |  |
| FootGroundContact_01_L_01 | 400 | — | — | 12 |
| LowerLegGroundContact_01_L_02 | — | — | — |  |
| FootGroundContact_01_L_02 | 400 | — | — | 12 |
| LowerLegGroundContact_01_L_03 | — | — | — |  |
| FootGroundContact_01_L_03 | 400 | — | — | 12 |
| LowerLegGroundContact_01_R_01 | — | — | — |  |
| FootGroundContact_01_R_01 | 400 | — | — | 12 |
| LowerLegGroundContact_01_R_02 | — | — | — |  |
| FootGroundContact_01_R_02 | 400 | — | — | 12 |
| LowerLegGroundContact_01_R_03 | — | — | — |  |
| FootGroundContact_01_R_03 | 400 | — | — | 12 |
| UpperLegGroundContact_01_L_01 | — | — | — |  |
| UpperLegGroundContact_01_L_02 | — | — | — |  |
| UpperLegGroundContact_01_L_03 | — | — | — |  |
| UpperLegGroundContact_01_R_01 | — | — | — |  |
| UpperLegGroundContact_01_R_02 | — | — | — |  |
| UpperLegGroundContact_01_R_03 | — | — | — |  |
| Body_01 | 23100 | Normal | 1 | 0 |
| Head_01 | 30000 | Normal | 1 | 2 |
| Core_01 | 30000 | Critical | 1.5 | 3 |
| Head_01_Armor_01_L_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_01_R_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_02_L_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_02_R_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_03_L_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_03_R_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_04_L_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_04_R_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_05_L_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Armor_05_R_01 | 300 | Armor | 0.4 | 10 |
| Head_01_Insides_01_L_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_01_R_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_02_L_01 | 5250 | Fragile | 1.2 | 5 |
| Head_01_Insides_02_R_01 | 5250 | Fragile | 1.2 | 5 |
| Weapon_Laser_01 | 150000 | Sturdy | 0.4 | 11 |
| Weapon_Laser_Armor_01 | 300 | Armor | 0.4 | 10 |
| Weapon_Laser_Barrel_01 | 150000 | Sturdy | 0.4 | 11 |
| Weapon_Launcher_01 | 150000 | Sturdy | 0.4 | 11 |
| UpperLeg_01_L_01 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_L_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_L_01 | 4050 | Normal | 1 | 1 |
| Ankle_01_L_01 | 400 | Normal | 1 | 12 |
| Foot_01_L_01 | 400 | Normal | 1 | 12 |
| Hydraulics_Foot_01_L_01 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_L_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_L_01 | 300 | Armor | 0.4 | 10 |
| LowerLeg_01_Insides_01_L_01 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_L_01 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_L_01 | 300 | Armor | 0.4 | 10 |
| UpperLeg_01_L_02 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_L_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_L_02 | 4050 | Normal | 1 | 1 |
| Ankle_01_L_02 | 400 | Normal | 1 | 12 |
| Foot_01_L_02 | 400 | Normal | 1 | 12 |
| Hydraulics_Foot_01_L_02 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_L_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_L_02 | 300 | Armor | 0.4 | 10 |
| LowerLeg_01_Insides_01_L_02 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_L_02 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_L_02 | 300 | Armor | 0.4 | 10 |
| UpperLeg_01_L_03 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_L_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_L_03 | 4050 | Normal | 1 | 1 |
| Ankle_01_L_03 | 400 | Normal | 1 | 12 |
| Foot_01_L_03 | 400 | Normal | 1 | 12 |
| Hydraulics_Foot_01_L_03 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_L_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_L_03 | 300 | Armor | 0.4 | 10 |
| LowerLeg_01_Insides_01_L_03 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_L_03 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_L_03 | 300 | Armor | 0.4 | 10 |
| UpperLeg_01_R_01 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_R_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_R_01 | 4050 | Normal | 1 | 1 |
| Ankle_01_R_01 | 400 | Normal | 1 | 12 |
| Foot_01_R_01 | 400 | Normal | 1 | 12 |
| Hydraulics_Foot_01_R_01 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_R_01 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_R_01 | 300 | Armor | 0.4 | 10 |
| LowerLeg_01_Insides_01_R_01 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_R_01 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_R_01 | 300 | Armor | 0.4 | 10 |
| UpperLeg_01_R_02 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_R_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_R_02 | 4050 | Normal | 1 | 1 |
| Ankle_01_R_02 | 400 | Normal | 1 | 12 |
| Foot_01_R_02 | 400 | Normal | 1 | 12 |
| Hydraulics_Foot_01_R_02 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_R_02 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_R_02 | 300 | Armor | 0.4 | 10 |
| LowerLeg_01_Insides_01_R_02 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_R_02 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_R_02 | 300 | Armor | 0.4 | 10 |
| UpperLeg_01_R_03 | 4050 | Normal | 1 | 1 |
| Hydraulics_UpperLeg_01_R_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_R_03 | 4050 | Normal | 1 | 1 |
| Ankle_01_R_03 | 400 | Normal | 1 | 12 |
| Foot_01_R_03 | 400 | Normal | 1 | 12 |
| Hydraulics_Foot_01_R_03 | 30000 | Normal | 1 | 7 |
| Hydraulics_UpperLeg_02_R_03 | 30000 | Normal | 1 | 7 |
| LowerLeg_01_Armor_01_R_03 | 300 | Armor | 0.4 | 10 |
| LowerLeg_01_Insides_01_R_03 | 1500 | Fragile | 1.2 | 6 |
| LowerLeg_01_Weakpoint_01_R_03 | 6000 | WeakPoint | 1.5 | 4 |
| UpperLeg_01_Armor_01_R_03 | 300 | Armor | 0.4 | 10 |
| EyeStaticMeshDummy | — | — | — |  |
| ID_Weapon_Blast | 0 | — | — | 9 |
| ID_Weapon_Laser | 0 | — | — | 8 |
| ID_Weapon_Shockwave | 0 | — | — | 8 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 23100 | Body_01 |
| 1 | ALL(ID.Leg, NONE(Group.Weakpoint)) | 4050 | UpperLeg_01_L_01, LowerLeg_01_L_01, UpperLeg_01_L_02, LowerLeg_01_L_02, UpperLeg_01_L_03, LowerLeg_01_L_03, UpperLeg_01_R_01, LowerLeg_01_R_01, UpperLeg_01_R_02, LowerLeg_01_R_02, UpperLeg_01_R_03, LowerLeg_01_R_03 |
| 2 | ID.Head | 30000 | Head_Laser_Socket, Head_01 |
| 3 | ANY(ID.Core) | 30000 | Core_01 |
| 4 | ANY(Group.Weakpoint) | 6000 | LowerLeg_01_Weakpoint_01_L_01, LowerLeg_01_Weakpoint_01_L_02, LowerLeg_01_Weakpoint_01_L_03, LowerLeg_01_Weakpoint_01_R_01, LowerLeg_01_Weakpoint_01_R_02, LowerLeg_01_Weakpoint_01_R_03 |
| 5 | HealthGroup.Base | 5250 | Head_01_Insides_01_L_01, Head_01_Insides_01_R_01, Head_01_Insides_02_L_01, Head_01_Insides_02_R_01 |
| 6 | HealthGroup.Legs | 1500 | LowerLeg_01_Insides_01_L_01, LowerLeg_01_Insides_01_L_02, LowerLeg_01_Insides_01_L_03, LowerLeg_01_Insides_01_R_01, LowerLeg_01_Insides_01_R_02, LowerLeg_01_Insides_01_R_03 |
| 7 | HealthGroup.SubParts | 30000 | Hydraulics_UpperLeg_01_L_01, Hydraulics_Foot_01_L_01, Hydraulics_UpperLeg_02_L_01, Hydraulics_UpperLeg_01_L_02, Hydraulics_Foot_01_L_02, Hydraulics_UpperLeg_02_L_02, Hydraulics_UpperLeg_01_L_03, Hydraulics_Foot_01_L_03, Hydraulics_UpperLeg_02_L_03, Hydraulics_UpperLeg_01_R_01, Hydraulics_Foot_01_R_01, Hydraulics_UpperLeg_02_R_01, Hydraulics_UpperLeg_01_R_02, Hydraulics_Foot_01_R_02, Hydraulics_UpperLeg_02_R_02, Hydraulics_UpperLeg_01_R_03, Hydraulics_Foot_01_R_03, Hydraulics_UpperLeg_02_R_03 |
| 8 | ANY(ID.Weapon.Shockwave, ID.Weapon.Laser) | 0 | ID_Weapon_Laser, ID_Weapon_Shockwave |
| 9 | ANY(ID.Weapon.Blast) | 0 | ID_Weapon_Blast |
| 10 | ANY(ID.Armor) | 300 | Head_01_Armor_01_L_01, Head_01_Armor_01_R_01, Head_01_Armor_02_L_01, Head_01_Armor_02_R_01, Head_01_Armor_03_L_01, Head_01_Armor_03_R_01, Head_01_Armor_04_L_01, Head_01_Armor_04_R_01, Head_01_Armor_05_L_01, Head_01_Armor_05_R_01, Weapon_Laser_Armor_01, LowerLeg_01_Armor_01_L_01, UpperLeg_01_Armor_01_L_01, LowerLeg_01_Armor_01_L_02, UpperLeg_01_Armor_01_L_02, LowerLeg_01_Armor_01_L_03, UpperLeg_01_Armor_01_L_03, LowerLeg_01_Armor_01_R_01, UpperLeg_01_Armor_01_R_01, LowerLeg_01_Armor_01_R_02, UpperLeg_01_Armor_01_R_02, LowerLeg_01_Armor_01_R_03, UpperLeg_01_Armor_01_R_03 |
| 11 | Part.HealthGroup.Indestructable | 150000 | Weapon_Launcher_Socket, Weapon_Laser_01, Weapon_Laser_Barrel_01, Weapon_Launcher_01 |
| 12 | ANY(ID.Foot, ID.Ankle) | 400 | FootGroundContact_01_L_01, FootGroundContact_01_L_02, FootGroundContact_01_L_03, FootGroundContact_01_R_01, FootGroundContact_01_R_02, FootGroundContact_01_R_03, Ankle_01_L_01, Foot_01_L_01, Ankle_01_L_02, Foot_01_L_02, Ankle_01_L_03, Foot_01_L_03, Ankle_01_R_01, Foot_01_R_01, Ankle_01_R_02, Foot_01_R_02, Ankle_01_R_03, Foot_01_R_03 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/MintType/Peppermint/CS_Peppermint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Peppermint/CS_Peppermint.json)
- [Content/Pioneer/Enemies/MintType/Peppermint/C_Peppermint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Peppermint/C_Peppermint.json)
- [Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/CSSC_Peppermint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/CSSC_Peppermint.json)
- [Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/DA_Balancing_C_Peppermint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/DA_Balancing_C_Peppermint.json)
- [Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/DA_EnemyMetaData_Peppermint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/DA_EnemyMetaData_Peppermint.json)
- [Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/DA_EnemyType_Peppermint.json](../Sources/PioneerGame/Content/Pioneer/Enemies/MintType/Peppermint/DataAssets/DA_EnemyType_Peppermint.json)

</details>
