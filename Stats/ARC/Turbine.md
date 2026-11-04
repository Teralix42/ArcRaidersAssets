# ARC Turbine

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 4000 HP. **Internal class:** `C_Monolith`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Turbine.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Turbine/01_Original_Materials_C.png"><img src="Renders/Turbine/01_Original_Materials_C.png" width="48%" alt="ARC Turbine: Original Materials"></a>
<a href="Renders/Turbine/03_Part_Health_C.png"><img src="Renders/Turbine/03_Part_Health_C.png" width="48%" alt="ARC Turbine: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Turbine/01_Original_Materials_A.png"><img src="Renders/Turbine/01_Original_Materials_A.png" width="31%" alt="Turbine original materials"></a>
  <a href="Renders/Turbine/01_Original_Materials_B.png"><img src="Renders/Turbine/01_Original_Materials_B.png" width="31%" alt="Turbine original materials"></a>
  <a href="Renders/Turbine/01_Original_Materials_C.png"><img src="Renders/Turbine/01_Original_Materials_C.png" width="31%" alt="Turbine original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Turbine/02_Part_Type_A.png"><img src="Renders/Turbine/02_Part_Type_A.png" width="31%" alt="Turbine part type"></a>
  <a href="Renders/Turbine/02_Part_Type_B.png"><img src="Renders/Turbine/02_Part_Type_B.png" width="31%" alt="Turbine part type"></a>
  <a href="Renders/Turbine/02_Part_Type_C.png"><img src="Renders/Turbine/02_Part_Type_C.png" width="31%" alt="Turbine part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Turbine/03_Part_Health_A.png"><img src="Renders/Turbine/03_Part_Health_A.png" width="31%" alt="Turbine part health"></a>
  <a href="Renders/Turbine/03_Part_Health_B.png"><img src="Renders/Turbine/03_Part_Health_B.png" width="31%" alt="Turbine part health"></a>
  <a href="Renders/Turbine/03_Part_Health_C.png"><img src="Renders/Turbine/03_Part_Health_C.png" width="31%" alt="Turbine part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Turbine/04_Break_Off_A.png"><img src="Renders/Turbine/04_Break_Off_A.png" width="31%" alt="Turbine break-off parts"></a>
  <a href="Renders/Turbine/04_Break_Off_B.png"><img src="Renders/Turbine/04_Break_Off_B.png" width="31%" alt="Turbine break-off parts"></a>
  <a href="Renders/Turbine/04_Break_Off_C.png"><img src="Renders/Turbine/04_Break_Off_C.png" width="31%" alt="Turbine break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Turbine/05_Scavenge_Interaction_A.png"><img src="Renders/Turbine/05_Scavenge_Interaction_A.png" width="31%" alt="Turbine scavenging"></a>
  <a href="Renders/Turbine/05_Scavenge_Interaction_B.png"><img src="Renders/Turbine/05_Scavenge_Interaction_B.png" width="31%" alt="Turbine scavenging"></a>
  <a href="Renders/Turbine/05_Scavenge_Interaction_C.png"><img src="Renders/Turbine/05_Scavenge_Interaction_C.png" width="31%" alt="Turbine scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Turbine/06_Damage_Targets_A.png"><img src="Renders/Turbine/06_Damage_Targets_A.png" width="31%" alt="Turbine damage targets"></a>
  <a href="Renders/Turbine/06_Damage_Targets_B.png"><img src="Renders/Turbine/06_Damage_Targets_B.png" width="31%" alt="Turbine damage targets"></a>
  <a href="Renders/Turbine/06_Damage_Targets_C.png"><img src="Renders/Turbine/06_Damage_Targets_C.png" width="31%" alt="Turbine damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core_A | 600 | WeakPoint | 1.5 |
| Core_B | 600 | WeakPoint | 1.5 |
| Core_C | 600 | WeakPoint | 1.5 |
| Core_D | 600 | WeakPoint | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| StrikeWeaponSocket_1 | — | — | — |  |
| StrikeWeaponSocket_2 | — | — | — |  |
| StrikeWeaponSocket_3 | — | — | — |  |
| StrikeWeaponSocket_4 | — | — | — |  |
| ActiveThrustSocket | — | — | — |  |
| Frame | 4000 | Sturdy | 0.4 | 0 |
| CenterSpinner | 5000 | Sturdy | 0.4 | 10 |
| Core_A | 600 | WeakPoint | 1.5 | 4 |
| CoreArmor_A | 50 | Armor | 0.4 | 7 |
| Core_B | 600 | WeakPoint | 1.5 | 4 |
| CoreArmor_B | 50 | Armor | 0.4 | 7 |
| Core_C | 600 | WeakPoint | 1.5 | 4 |
| CoreArmor_C | 50 | Armor | 0.4 | 7 |
| Core_D | 600 | WeakPoint | 1.5 | 4 |
| CoreArmor_D | 50 | Armor | 0.4 | 7 |
| Fan | 350 | Sturdy | 0.4 | 3 |
| Head | 90000 | Sturdy | 0.4 | 11 |
| Hydraulic_LowerLeg_01_A | 350 | Sturdy | 0.4 | 3 |
| Hydraulic_LowerLeg_01_B | 350 | Sturdy | 0.4 | 3 |
| Hydraulic_LowerLeg_01_C | 350 | Sturdy | 0.4 | 3 |
| Hydraulic_LowerLeg_01_D | 350 | Sturdy | 0.4 | 3 |
| Piston | 350 | Sturdy | 0.4 | 3 |
| SubFrame_01_A | 1200 | Sturdy | 0.4 | 13 |
| Armor_01_A | 350 | Armor | 0.4 | 3 |
| Armor_02_A | 40 | Armor | 0.4 | 1 |
| Armor_03_A | 40 | Armor | 0.4 | 1 |
| Duct_01_A | 600 | Armor | 0.4 | 12 |
| Flap_01_A | 150 | Normal | 1 | 8 |
| UpperLeg_01_A | 640 | Sturdy | 0.4 | 5 |
| Armor_04_A | 350 | Armor | 0.4 | 3 |
| Armor_05_A | 40 | Armor | 0.4 | 1 |
| Hydraulic_LowerLeg_02_A | 350 | Sturdy | 0.4 | 3 |
| LowerLeg_01_A | 320 | Sturdy | 0.4 | 6 |
| Armor_06_A | 350 | Armor | 0.4 | 3 |
| Foot_A | 320 | Sturdy | 0.4 | 9 |
| HydraulicsFoot_A | 350 | Sturdy | 0.4 | 3 |
| SubFrame_01_B | 1200 | Sturdy | 0.4 | 13 |
| Armor_01_B | 350 | Armor | 0.4 | 3 |
| Armor_02_B | 40 | Armor | 0.4 | 1 |
| Armor_03_B | 40 | Armor | 0.4 | 1 |
| Duct_01_B | 600 | Armor | 0.4 | 12 |
| Flap_01_B | 150 | Normal | 1 | 8 |
| UpperLeg_01_B | 640 | Sturdy | 0.4 | 5 |
| Armor_04_B | 350 | Armor | 0.4 | 3 |
| Armor_05_B | 40 | Armor | 0.4 | 1 |
| Hydraulic_LowerLeg_02_B | 350 | Sturdy | 0.4 | 3 |
| LowerLeg_01_B | 320 | Sturdy | 0.4 | 6 |
| Armor_06_B | 350 | Armor | 0.4 | 3 |
| Foot_B | 320 | Sturdy | 0.4 | 9 |
| HydraulicsFoot_B | 350 | Sturdy | 0.4 | 3 |
| SubFrame_01_C | 1200 | Sturdy | 0.4 | 13 |
| Armor_01_C | 350 | Armor | 0.4 | 3 |
| Armor_02_C | 40 | Armor | 0.4 | 1 |
| Armor_03_C | 40 | Armor | 0.4 | 1 |
| Duct_01_C | 600 | Armor | 0.4 | 12 |
| Flap_01_C | 150 | Normal | 1 | 8 |
| UpperLeg_01_C | 640 | Sturdy | 0.4 | 5 |
| Armor_04_C | 350 | Armor | 0.4 | 3 |
| Armor_05_C | 40 | Armor | 0.4 | 1 |
| Hydraulic_LowerLeg_02_C | 350 | Sturdy | 0.4 | 3 |
| LowerLeg_01_C | 320 | Sturdy | 0.4 | 6 |
| Armor_06_C | 350 | Armor | 0.4 | 3 |
| Foot_C | 320 | Sturdy | 0.4 | 9 |
| HydraulicsFoot_C | 350 | Sturdy | 0.4 | 3 |
| SubFrame_01_D | 1200 | Sturdy | 0.4 | 13 |
| Armor_01_D | 350 | Armor | 0.4 | 3 |
| Armor_02_D | 40 | Armor | 0.4 | 1 |
| Armor_03_D | 40 | Armor | 0.4 | 1 |
| Duct_01_D | 600 | Armor | 0.4 | 12 |
| Flap_01_D | 150 | Normal | 1 | 8 |
| UpperLeg_01_D | 640 | Sturdy | 0.4 | 5 |
| Armor_04_D | 350 | Armor | 0.4 | 3 |
| Armor_05_D | 40 | Armor | 0.4 | 1 |
| Hydraulic_LowerLeg_02_D | 350 | Sturdy | 0.4 | 3 |
| LowerLeg_01_D | 320 | Sturdy | 0.4 | 6 |
| Armor_06_D | 350 | Armor | 0.4 | 3 |
| Foot_D | 320 | Sturdy | 0.4 | 9 |
| HydraulicsFoot_D | 350 | Sturdy | 0.4 | 3 |
| ThrusterBase | 90000 | Armor | 0.4 | 2 |
| ThrusterPart_A | 90000 | Armor | 0.4 | 2 |
| ThrusterPart_B | 90000 | Armor | 0.4 | 2 |
| ThrusterPart_C | 90000 | Armor | 0.4 | 2 |
| ThrusterShield | 350 | Armor | 0.4 | 3 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ANY(ID.Frame) | 4000 | Frame |
| 1 | ANY(ID.Armor.Medium) | 40 | Armor_02_A, Armor_03_A, Armor_05_A, Armor_02_B, Armor_03_B, Armor_05_B, Armor_02_C, Armor_03_C, Armor_05_C, Armor_02_D, Armor_03_D, Armor_05_D |
| 2 | ID.Thruster | 90000 | ThrusterBase, ThrusterPart_A, ThrusterPart_B, ThrusterPart_C |
| 3 | ID.Armor.Heavy | 350 | Fan, Hydraulic_LowerLeg_01_A, Hydraulic_LowerLeg_01_B, Hydraulic_LowerLeg_01_C, Hydraulic_LowerLeg_01_D, Piston, Armor_01_A, Armor_04_A, Hydraulic_LowerLeg_02_A, Armor_06_A, HydraulicsFoot_A, Armor_01_B, Armor_04_B, Hydraulic_LowerLeg_02_B, Armor_06_B, HydraulicsFoot_B, Armor_01_C, Armor_04_C, Hydraulic_LowerLeg_02_C, Armor_06_C, HydraulicsFoot_C, Armor_01_D, Armor_04_D, Hydraulic_LowerLeg_02_D, Armor_06_D, HydraulicsFoot_D, ThrusterShield |
| 4 | ID.Core | 600 | Core_A, Core_B, Core_C, Core_D |
| 5 | ALL(ID.Leg, Group.Relative.Upper) | 640 | UpperLeg_01_A, UpperLeg_01_B, UpperLeg_01_C, UpperLeg_01_D |
| 6 | ALL(ID.Leg, Group.Relative.Lower) | 320 | LowerLeg_01_A, LowerLeg_01_B, LowerLeg_01_C, LowerLeg_01_D |
| 7 | ID.Armor.Core | 50 | CoreArmor_A, CoreArmor_B, CoreArmor_C, CoreArmor_D |
| 8 | ID.Flap.Medium | 150 | Flap_01_A, Flap_01_B, Flap_01_C, Flap_01_D |
| 9 | ID.Foot | 320 | Foot_A, Foot_B, Foot_C, Foot_D |
| 10 | ID.Spinner | 5000 | CenterSpinner |
| 11 | ID.Armor.Head | 90000 | Head |
| 12 | ID.Armor.Body | 600 | Duct_01_A, Duct_01_B, Duct_01_C, Duct_01_D |
| 13 | ID.Subframe | 1200 | SubFrame_01_A, SubFrame_01_B, SubFrame_01_C, SubFrame_01_D |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Monolith/Monolith/Art/CSSC_Monolith.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Monolith/Monolith/Art/CSSC_Monolith.json)
- [Content/Pioneer/Enemies/Monolith/Monolith/C_Monolith.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Monolith/Monolith/C_Monolith.json)
- [Content/Pioneer/Enemies/Monolith/Monolith/DataAssets/DA_Balancing_C_Monolith.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Monolith/Monolith/DataAssets/DA_Balancing_C_Monolith.json)
- [Content/Pioneer/Enemies/Monolith/Monolith/DataAssets/DA_EnemyMetaData_Monolith.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Monolith/Monolith/DataAssets/DA_EnemyMetaData_Monolith.json)
- [Content/Pioneer/Enemies/Monolith/Monolith/DataAssets/DA_EnemyType_Monolith.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Monolith/Monolith/DataAssets/DA_EnemyType_Monolith.json)

</details>
