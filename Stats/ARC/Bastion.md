# Bastion

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 2050 HP. **Internal class:** `C_Chonk`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Bastion.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Bastion/01_Original_Materials_C.png"><img src="Renders/Bastion/01_Original_Materials_C.png" width="48%" alt="Bastion: Original Materials"></a>
<a href="Renders/Bastion/03_Part_Health_C.png"><img src="Renders/Bastion/03_Part_Health_C.png" width="48%" alt="Bastion: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Core + limb structure |
| B | Without armor |
| C | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Core + limb structure**

<a href="Renders/Bastion/01_Original_Materials_A.png"><img src="Renders/Bastion/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Bastion/02_Part_Type_A.png"><img src="Renders/Bastion/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Bastion/03_Part_Health_A.png"><img src="Renders/Bastion/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Bastion/04_Break_Off_A.png"><img src="Renders/Bastion/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Bastion/05_Scavenge_Interaction_A.png"><img src="Renders/Bastion/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Bastion/06_Damage_Targets_A.png"><img src="Renders/Bastion/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Without armor**

<a href="Renders/Bastion/01_Original_Materials_B.png"><img src="Renders/Bastion/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Bastion/02_Part_Type_B.png"><img src="Renders/Bastion/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Bastion/03_Part_Health_B.png"><img src="Renders/Bastion/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Bastion/04_Break_Off_B.png"><img src="Renders/Bastion/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Bastion/05_Scavenge_Interaction_B.png"><img src="Renders/Bastion/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Bastion/06_Damage_Targets_B.png"><img src="Renders/Bastion/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

**C: Full model**

<a href="Renders/Bastion/01_Original_Materials_C.png"><img src="Renders/Bastion/01_Original_Materials_C.png" width="32%" alt="Original Materials, layer C"></a>
<a href="Renders/Bastion/02_Part_Type_C.png"><img src="Renders/Bastion/02_Part_Type_C.png" width="32%" alt="Part Type, layer C"></a>
<a href="Renders/Bastion/03_Part_Health_C.png"><img src="Renders/Bastion/03_Part_Health_C.png" width="32%" alt="Part Health, layer C"></a>
<a href="Renders/Bastion/04_Break_Off_C.png"><img src="Renders/Bastion/04_Break_Off_C.png" width="32%" alt="Break Off, layer C"></a>
<a href="Renders/Bastion/05_Scavenge_Interaction_C.png"><img src="Renders/Bastion/05_Scavenge_Interaction_C.png" width="32%" alt="Scavenge Interaction, layer C"></a>
<a href="Renders/Bastion/06_Damage_Targets_C.png"><img src="Renders/Bastion/06_Damage_Targets_C.png" width="32%" alt="Damage Targets, layer C"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core | 5000 | Critical | 1.5 |
| Weakpoint_02 | 450 | WeakPoint | 1.5 |
| Weakpoint_01_L_01 | 180 | WeakPoint | 1.5 |
| Weakpoint_01_L_02 | 180 | WeakPoint | 1.5 |
| Weakpoint_01_L_03 | 180 | WeakPoint | 1.5 |
| Weakpoint_01_R_01 | 180 | WeakPoint | 1.5 |
| Weakpoint_01_R_02 | 180 | WeakPoint | 1.5 |
| Weakpoint_01_R_03 | 180 | WeakPoint | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Muzzle | — | — | — |  |
| Sensor | — | — | — |  |
| Body_01 | 2050 | Normal | 1 | 0 |
| HeadPivot | 1e+07 | Normal | 1 | 11 |
| Head_01 | 10000 | Normal | 1 | 6 |
| Core | 5000 | Critical | 1.5 | 12 |
| Head_01_Armor_01_L_01 | 500 | Armor | 0.4 | 4 |
| Head_01_Armor_01_R_01 | 500 | Armor | 0.4 | 4 |
| Head_01_Armor_02_L_01 | 500 | Armor | 0.4 | 4 |
| Head_01_Armor_02_R_01 | 500 | Armor | 0.4 | 4 |
| Insides_01_L_01 | 250 | Fragile | 1.2 | 10 |
| Insides_01_R_01 | 250 | Fragile | 1.2 | 10 |
| Insides_02 | 10000 | Fragile | 1.2 | 13 |
| Weakpoint_02 | 450 | WeakPoint | 1.5 | 1 |
| Weapon_Pivot_01 | 10000 | Sturdy | 0.4 | 8 |
| Weapon_01_Armor_01_L_01 | 500 | Armor | 0.4 | 4 |
| Weapon_01_Armor_01_R_01 | 500 | Armor | 0.4 | 4 |
| Weapon_01_Barrel_01 | 10000 | Sturdy | 0.4 | 7 |
| UpperLeg_01_L_01 | 280 | Normal | 1 | 2 |
| LowerLeg_01_L_01 | 180 | Normal | 1 | 3 |
| LowerLeg_01_Armor_01_L_01 | 48 | Armor | 0.4 | 5 |
| Foot_L_01 | — | Normal | 1 |  |
| UpperLeg_01_Armor_01_L_01 | 48 | Armor | 0.4 | 5 |
| Weakpoint_01_L_01 | 180 | WeakPoint | 1.5 | 9 |
| UpperLeg_01_L_02 | 280 | Normal | 1 | 2 |
| LowerLeg_01_L_02 | 180 | Normal | 1 | 3 |
| LowerLeg_01_Armor_01_L_02 | 48 | Armor | 0.4 | 5 |
| Foot_L_02 | — | Normal | 1 |  |
| UpperLeg_01_Armor_01_L_02 | 48 | Armor | 0.4 | 5 |
| Weakpoint_01_L_02 | 180 | WeakPoint | 1.5 | 9 |
| UpperLeg_01_L_03 | 280 | Normal | 1 | 2 |
| LowerLeg_01_L_03 | 180 | Normal | 1 | 3 |
| LowerLeg_01_Armor_01_L_03 | 48 | Armor | 0.4 | 5 |
| Foot_L_03 | — | Normal | 1 |  |
| UpperLeg_01_Armor_01_L_03 | 48 | Armor | 0.4 | 5 |
| Weakpoint_01_L_03 | 180 | WeakPoint | 1.5 | 9 |
| UpperLeg_01_R_01 | 280 | Normal | 1 | 2 |
| LowerLeg_01_R_01 | 180 | Normal | 1 | 3 |
| LowerLeg_01_Armor_01_R_01 | 48 | Armor | 0.4 | 5 |
| Foot_R_01 | — | Normal | 1 |  |
| UpperLeg_01_Armor_01_R_01 | 48 | Armor | 0.4 | 5 |
| Weakpoint_01_R_01 | 180 | WeakPoint | 1.5 | 9 |
| UpperLeg_01_R_02 | 280 | Normal | 1 | 2 |
| LowerLeg_01_R_02 | 180 | Normal | 1 | 3 |
| LowerLeg_01_Armor_01_R_02 | 48 | Armor | 0.4 | 5 |
| Foot_R_02 | — | Normal | 1 |  |
| UpperLeg_01_Armor_01_R_02 | 48 | Armor | 0.4 | 5 |
| Weakpoint_01_R_02 | 180 | WeakPoint | 1.5 | 9 |
| UpperLeg_01_R_03 | 280 | Normal | 1 | 2 |
| LowerLeg_01_R_03 | 180 | Normal | 1 | 3 |
| LowerLeg_01_Armor_01_R_03 | 48 | Armor | 0.4 | 5 |
| Foot_R_03 | — | Normal | 1 |  |
| UpperLeg_01_Armor_01_R_03 | 48 | Armor | 0.4 | 5 |
| Weakpoint_01_R_03 | 180 | WeakPoint | 1.5 | 9 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 2050 | Body_01 |
| 1 | Group.Weakpoint | 450 | Weakpoint_02 |
| 2 | ALL(ID.Leg, Group.Relative.Upper) | 280 | UpperLeg_01_L_01, UpperLeg_01_L_02, UpperLeg_01_L_03, UpperLeg_01_R_01, UpperLeg_01_R_02, UpperLeg_01_R_03 |
| 3 | ALL(ID.Leg, Group.Relative.Lower) | 180 | LowerLeg_01_L_01, LowerLeg_01_L_02, LowerLeg_01_L_03, LowerLeg_01_R_01, LowerLeg_01_R_02, LowerLeg_01_R_03 |
| 4 | ALL(ID.Armor.Heavy, NONE(HealthGroup.SubParts.01)) | 500 | Head_01_Armor_01_L_01, Head_01_Armor_01_R_01, Head_01_Armor_02_L_01, Head_01_Armor_02_R_01, Weapon_01_Armor_01_L_01, Weapon_01_Armor_01_R_01 |
| 5 | ID.Armor.Medium | 48 | LowerLeg_01_Armor_01_L_01, UpperLeg_01_Armor_01_L_01, LowerLeg_01_Armor_01_L_02, UpperLeg_01_Armor_01_L_02, LowerLeg_01_Armor_01_L_03, UpperLeg_01_Armor_01_L_03, LowerLeg_01_Armor_01_R_01, UpperLeg_01_Armor_01_R_01, LowerLeg_01_Armor_01_R_02, UpperLeg_01_Armor_01_R_02, LowerLeg_01_Armor_01_R_03, UpperLeg_01_Armor_01_R_03 |
| 6 | ID.Head | 10000 | Head_01 |
| 7 | ID.Turret | 10000 | Weapon_01_Barrel_01 |
| 8 | ID.Arm.Front | 10000 | Weapon_Pivot_01 |
| 9 | ANY(ID.Joint) | 180 | Weakpoint_01_L_01, Weakpoint_01_L_02, Weakpoint_01_L_03, Weakpoint_01_R_01, Weakpoint_01_R_02, Weakpoint_01_R_03 |
| 10 | HealthGroup.Base | 250 | Insides_01_L_01, Insides_01_R_01 |
| 11 | ANY(ID.HeadPivot) | 1e+07 | HeadPivot |
| 12 | ID.Core | 5000 | Core |
| 13 | HealthGroup.SubParts.01 | 10000 | Insides_02 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Chonk/C_Chonk.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Chonk/C_Chonk.json)
- [Content/Pioneer/Enemies/Chonk/Chonk_01/CSSM_Chonk_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Chonk/Chonk_01/CSSM_Chonk_01.json)
- [Content/Pioneer/Enemies/Chonk/DataAssets/DA_Balancing_C_Chonk.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Chonk/DataAssets/DA_Balancing_C_Chonk.json)
- [Content/Pioneer/Enemies/Chonk/DataAssets/DA_EnemyMetaData_Chonk.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Chonk/DataAssets/DA_EnemyMetaData_Chonk.json)
- [Content/Pioneer/Enemies/Chonk/DataAssets/DA_EnemyType_Chonk.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Chonk/DataAssets/DA_EnemyType_Chonk.json)

</details>
