# Leaper

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 1100 HP. **Internal class:** `C_BullCrab_01`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Leaper.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Leaper/01_Original_Materials_C.png"><img src="Renders/Leaper/01_Original_Materials_C.png" width="48%" alt="Leaper: Original Materials"></a>
<a href="Renders/Leaper/03_Part_Health_C.png"><img src="Renders/Leaper/03_Part_Health_C.png" width="48%" alt="Leaper: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Leaper/01_Original_Materials_A.png"><img src="Renders/Leaper/01_Original_Materials_A.png" width="31%" alt="Leaper original materials"></a>
  <a href="Renders/Leaper/01_Original_Materials_B.png"><img src="Renders/Leaper/01_Original_Materials_B.png" width="31%" alt="Leaper original materials"></a>
  <a href="Renders/Leaper/01_Original_Materials_C.png"><img src="Renders/Leaper/01_Original_Materials_C.png" width="31%" alt="Leaper original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Leaper/02_Part_Type_A.png"><img src="Renders/Leaper/02_Part_Type_A.png" width="31%" alt="Leaper part type"></a>
  <a href="Renders/Leaper/02_Part_Type_B.png"><img src="Renders/Leaper/02_Part_Type_B.png" width="31%" alt="Leaper part type"></a>
  <a href="Renders/Leaper/02_Part_Type_C.png"><img src="Renders/Leaper/02_Part_Type_C.png" width="31%" alt="Leaper part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Leaper/03_Part_Health_A.png"><img src="Renders/Leaper/03_Part_Health_A.png" width="31%" alt="Leaper part health"></a>
  <a href="Renders/Leaper/03_Part_Health_B.png"><img src="Renders/Leaper/03_Part_Health_B.png" width="31%" alt="Leaper part health"></a>
  <a href="Renders/Leaper/03_Part_Health_C.png"><img src="Renders/Leaper/03_Part_Health_C.png" width="31%" alt="Leaper part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Leaper/04_Break_Off_A.png"><img src="Renders/Leaper/04_Break_Off_A.png" width="31%" alt="Leaper break-off parts"></a>
  <a href="Renders/Leaper/04_Break_Off_B.png"><img src="Renders/Leaper/04_Break_Off_B.png" width="31%" alt="Leaper break-off parts"></a>
  <a href="Renders/Leaper/04_Break_Off_C.png"><img src="Renders/Leaper/04_Break_Off_C.png" width="31%" alt="Leaper break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Leaper/05_Scavenge_Interaction_A.png"><img src="Renders/Leaper/05_Scavenge_Interaction_A.png" width="31%" alt="Leaper scavenging"></a>
  <a href="Renders/Leaper/05_Scavenge_Interaction_B.png"><img src="Renders/Leaper/05_Scavenge_Interaction_B.png" width="31%" alt="Leaper scavenging"></a>
  <a href="Renders/Leaper/05_Scavenge_Interaction_C.png"><img src="Renders/Leaper/05_Scavenge_Interaction_C.png" width="31%" alt="Leaper scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Leaper/06_Damage_Targets_A.png"><img src="Renders/Leaper/06_Damage_Targets_A.png" width="31%" alt="Leaper damage targets"></a>
  <a href="Renders/Leaper/06_Damage_Targets_B.png"><img src="Renders/Leaper/06_Damage_Targets_B.png" width="31%" alt="Leaper damage targets"></a>
  <a href="Renders/Leaper/06_Damage_Targets_C.png"><img src="Renders/Leaper/06_Damage_Targets_C.png" width="31%" alt="Leaper damage targets"></a>
</p>

</details>

### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| CoreSocket | — | — | — |  |
| Body | 1100 | Armor | 0.4 | 1 |
| Core | 2000 | Normal | 1 | 2 |
| Armor_01_C_01 | 16 | Armor | 0.4 | 6 |
| Armor_01_C_02 | 16 | Armor | 0.4 | 6 |
| Armor_01_C_03 | 16 | Armor | 0.4 | 6 |
| Armor_02 | 16 | Armor | 0.4 | 6 |
| Jaw_01_L_01 | 24 | Normal | 1 | 9 |
| Jaw_01_L_02 | 24 | Normal | 1 | 9 |
| Jaw_01_R_01 | 24 | Normal | 1 | 9 |
| Jaw_01_R_02 | 24 | Normal | 1 | 9 |
| Cylinder_01_L_01 | 24 | Normal | 1 | 9 |
| Cylinder_01_L_02 | 24 | Normal | 1 | 9 |
| Cylinder_01_L_03 | 24 | Normal | 1 | 9 |
| Cylinder_01_L_04 | 24 | Normal | 1 | 9 |
| Cylinder_01_R_01 | 24 | Normal | 1 | 9 |
| Cylinder_01_R_02 | 24 | Normal | 1 | 9 |
| Cylinder_01_R_03 | 24 | Normal | 1 | 9 |
| Cylinder_01_R_04 | 24 | Normal | 1 | 9 |
| Thruster_01_C_01 | 5000 | Sturdy | 0.4 | 0 |
| Thruster_01_C_02 | 5000 | Sturdy | 0.4 | 0 |
| UpperLeg_L_01 | 240 | Fragile | 1.2 | 3 |
| Armor_07_L_01 | 48 | Armor | 0.4 | 5 |
| Insides_01_L_01 | 100 | Fragile | 1.2 | 8 |
| LowerLeg_L_01 | 160 | Fragile | 1.2 | 4 |
| Armor_03_L_01 | 48 | Armor | 0.4 | 5 |
| Armor_06_L_01 | 6 | Armor | 0.4 | 7 |
| Armor_04_L_01 | 6 | Armor | 0.4 | 7 |
| Armor_05_L_01 | 48 | Armor | 0.4 | 5 |
| Insides_02_L_01 | 100 | Fragile | 1.2 | 8 |
| Insides_03_L_01 | 100 | Fragile | 1.2 | 8 |
| SOCKET_Foot_L_01 | — | Normal | 1 |  |
| UpperLeg_L_02 | 240 | Fragile | 1.2 | 3 |
| Armor_07_L_02 | 48 | Armor | 0.4 | 5 |
| Insides_01_L_02 | 100 | Fragile | 1.2 | 8 |
| LowerLeg_L_02 | 160 | Fragile | 1.2 | 4 |
| Armor_03_L_02 | 48 | Armor | 0.4 | 5 |
| Armor_06_L_02 | 6 | Armor | 0.4 | 7 |
| Armor_04_L_02 | 6 | Armor | 0.4 | 7 |
| Armor_05_L_02 | 48 | Armor | 0.4 | 5 |
| Insides_02_L_02 | 100 | Fragile | 1.2 | 8 |
| Insides_03_L_02 | 100 | Fragile | 1.2 | 8 |
| SOCKET_Foot_L_02 | — | Normal | 1 |  |
| UpperLeg_R_01 | 240 | Fragile | 1.2 | 3 |
| Armor_07_R_01 | 48 | Armor | 0.4 | 5 |
| Insides_01_R_01 | 100 | Fragile | 1.2 | 8 |
| LowerLeg_R_01 | 160 | Fragile | 1.2 | 4 |
| Armor_03_R_01 | 48 | Armor | 0.4 | 5 |
| Armor_06_R_01 | 6 | Armor | 0.4 | 7 |
| Armor_04_R_01 | 6 | Armor | 0.4 | 7 |
| Armor_05_R_01 | 48 | Armor | 0.4 | 5 |
| Insides_02_R_01 | 100 | Fragile | 1.2 | 8 |
| Insides_03_R_01 | 100 | Fragile | 1.2 | 8 |
| SOCKET_Foot_R_01 | — | Normal | 1 |  |
| UpperLeg_R_02 | 240 | Fragile | 1.2 | 3 |
| Armor_07_R_02 | 48 | Armor | 0.4 | 5 |
| Insides_01_R_02 | 100 | Fragile | 1.2 | 8 |
| LowerLeg_R_02 | 160 | Fragile | 1.2 | 4 |
| Armor_03_R_02 | 48 | Armor | 0.4 | 5 |
| Armor_06_R_02 | 6 | Armor | 0.4 | 7 |
| Armor_04_R_02 | 6 | Armor | 0.4 | 7 |
| Armor_05_R_02 | 48 | Armor | 0.4 | 5 |
| Insides_02_R_02 | 100 | Fragile | 1.2 | 8 |
| Insides_03_R_02 | 100 | Fragile | 1.2 | 8 |
| SOCKET_Foot_R_02 | — | Normal | 1 |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | Group.Indestructible | 5000 | Thruster_01_C_01, Thruster_01_C_02 |
| 1 | ID.Frame | 1100 | Body |
| 2 | ID.Core | 2000 | Core |
| 3 | ALL(ID.Leg, Group.Relative.Upper) | 240 | UpperLeg_L_01, UpperLeg_L_02, UpperLeg_R_01, UpperLeg_R_02 |
| 4 | ALL(ID.Leg, Group.Relative.Lower) | 160 | LowerLeg_L_01, LowerLeg_L_02, LowerLeg_R_01, LowerLeg_R_02 |
| 5 | ID.Armor.Heavy | 48 | Armor_07_L_01, Armor_03_L_01, Armor_05_L_01, Armor_07_L_02, Armor_03_L_02, Armor_05_L_02, Armor_07_R_01, Armor_03_R_01, Armor_05_R_01, Armor_07_R_02, Armor_03_R_02, Armor_05_R_02 |
| 6 | ID.Armor.Medium | 16 | Armor_01_C_01, Armor_01_C_02, Armor_01_C_03, Armor_02 |
| 7 | ID.Armor.Light | 6 | Armor_06_L_01, Armor_04_L_01, Armor_06_L_02, Armor_04_L_02, Armor_06_R_01, Armor_04_R_01, Armor_06_R_02, Armor_04_R_02 |
| 8 | HealthGroup.Base | 100 | Insides_01_L_01, Insides_02_L_01, Insides_03_L_01, Insides_01_L_02, Insides_02_L_02, Insides_03_L_02, Insides_01_R_01, Insides_02_R_01, Insides_03_R_01, Insides_01_R_02, Insides_02_R_02, Insides_03_R_02 |
| 9 | HealthGroup.SubParts | 24 | Jaw_01_L_01, Jaw_01_L_02, Jaw_01_R_01, Jaw_01_R_02, Cylinder_01_L_01, Cylinder_01_L_02, Cylinder_01_L_03, Cylinder_01_L_04, Cylinder_01_R_01, Cylinder_01_R_02, Cylinder_01_R_03, Cylinder_01_R_04 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Bullcrab/CSSC_BullCrab_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Bullcrab/CSSC_BullCrab_01.json)
- [Content/Pioneer/Enemies/Bullcrab/C_BullCrab_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Bullcrab/C_BullCrab_01.json)
- [Content/Pioneer/Enemies/Bullcrab/DA_Balancing_C_BullCrab_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Bullcrab/DA_Balancing_C_BullCrab_01.json)
- [Content/Pioneer/Enemies/Bullcrab/DA_EnemyMetaData_BullCrab.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Bullcrab/DA_EnemyMetaData_BullCrab.json)
- [Content/Pioneer/Enemies/Bullcrab/DA_EnemyType_BullCrab.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Bullcrab/DA_EnemyType_BullCrab.json)

</details>
