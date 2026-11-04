# Comet

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 150 HP. **Internal class:** `C_Rollbot_Boom`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Comet.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Comet/01_Original_Materials_C.png"><img src="Renders/Comet/01_Original_Materials_C.png" width="48%" alt="Comet: Original Materials"></a>
<a href="Renders/Comet/03_Part_Health_C.png"><img src="Renders/Comet/03_Part_Health_C.png" width="48%" alt="Comet: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Comet/01_Original_Materials_B.png"><img src="Renders/Comet/01_Original_Materials_B.png" width="47%" alt="Comet original materials"></a>
  <a href="Renders/Comet/01_Original_Materials_C.png"><img src="Renders/Comet/01_Original_Materials_C.png" width="47%" alt="Comet original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Comet/02_Part_Type_B.png"><img src="Renders/Comet/02_Part_Type_B.png" width="47%" alt="Comet part type"></a>
  <a href="Renders/Comet/02_Part_Type_C.png"><img src="Renders/Comet/02_Part_Type_C.png" width="47%" alt="Comet part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Comet/03_Part_Health_B.png"><img src="Renders/Comet/03_Part_Health_B.png" width="47%" alt="Comet part health"></a>
  <a href="Renders/Comet/03_Part_Health_C.png"><img src="Renders/Comet/03_Part_Health_C.png" width="47%" alt="Comet part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Comet/04_Break_Off_B.png"><img src="Renders/Comet/04_Break_Off_B.png" width="47%" alt="Comet break-off parts"></a>
  <a href="Renders/Comet/04_Break_Off_C.png"><img src="Renders/Comet/04_Break_Off_C.png" width="47%" alt="Comet break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Comet/05_Scavenge_Interaction_B.png"><img src="Renders/Comet/05_Scavenge_Interaction_B.png" width="47%" alt="Comet scavenging"></a>
  <a href="Renders/Comet/05_Scavenge_Interaction_C.png"><img src="Renders/Comet/05_Scavenge_Interaction_C.png" width="47%" alt="Comet scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Comet/06_Damage_Targets_B.png"><img src="Renders/Comet/06_Damage_Targets_B.png" width="47%" alt="Comet damage targets"></a>
  <a href="Renders/Comet/06_Damage_Targets_C.png"><img src="Renders/Comet/06_Damage_Targets_C.png" width="47%" alt="Comet damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core | 150 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| DummyParent_Root | 1000 | Normal | 1 | 3 |
| DummyFrame | 150 | Normal | 1 | 2 |
| Frame_L | 3000 | Normal | 1 | 4 |
| Armor_01_L | 10 | Armor | 0.4 | 0 |
| Armor_02_L | 10 | Armor | 0.4 | 0 |
| Armor_03_L | 10 | Armor | 0.4 | 0 |
| SideCylinder_L_01 | — | Normal | 1 |  |
| SideCylinder_L_02 | — | Normal | 1 |  |
| SideCylinder_L_03 | — | Normal | 1 |  |
| SideCylinder_L_04 | — | Normal | 1 |  |
| SideCylinder_L_05 | — | Normal | 1 |  |
| SideCylinder_L_06 | — | Normal | 1 |  |
| SubFrame_01_C | 150 | Normal | 1 | 5 |
| SubFrame_02_L | 150 | Normal | 1 | 5 |
| Frame_R | 3000 | Normal | 1 | 4 |
| Armor_01_R | 10 | Armor | 0.4 | 0 |
| Armor_02_R | 10 | Armor | 0.4 | 0 |
| Armor_03_R | 10 | Armor | 0.4 | 0 |
| SideCylinder_R_01 | — | Normal | 1 |  |
| SideCylinder_R_02 | — | Normal | 1 |  |
| SideCylinder_R_03 | — | Normal | 1 |  |
| SideCylinder_R_04 | — | Normal | 1 |  |
| SideCylinder_R_05 | — | Normal | 1 |  |
| SideCylinder_R_06 | — | Normal | 1 |  |
| SubFrame_02_R | 150 | Normal | 1 | 5 |
| FrameCenterAxis | 3000 | Normal | 1 | 4 |
| Arm_L | 10 | Normal | 1 | 0 |
| Arm_R | 10 | Normal | 1 | 0 |
| Core | 150 | Critical | 1.5 | 1 |
| Hull_01 | 150 | Normal | 1 | 5 |
| VisionConeDummy | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Armor.Heavy | 10 | Armor_01_L, Armor_02_L, Armor_03_L, Armor_01_R, Armor_02_R, Armor_03_R, Arm_L, Arm_R |
| 1 | ID.Core | 150 | Core |
| 2 | ID.Frame | 150 | DummyFrame |
| 3 | ID.Rollbot.Root | 1000 | DummyParent_Root |
| 4 | Group.Indestructible | 3000 | Frame_L, Frame_R, FrameCenterAxis |
| 5 | Group.Relative.Middle | 150 | SubFrame_01_C, SubFrame_02_L, SubFrame_02_R, Hull_01 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/RollBot/Boom/Art/CSSC_Boom_01_B.json](../Sources/PioneerGame/Content/Pioneer/Enemies/RollBot/Boom/Art/CSSC_Boom_01_B.json)
- [Content/Pioneer/Enemies/RollBot/Boom/CS_Boom.json](../Sources/PioneerGame/Content/Pioneer/Enemies/RollBot/Boom/CS_Boom.json)
- [Content/Pioneer/Enemies/RollBot/Boom/C_Rollbot_Boom.json](../Sources/PioneerGame/Content/Pioneer/Enemies/RollBot/Boom/C_Rollbot_Boom.json)
- [Content/Pioneer/Enemies/RollBot/Boom/DataAssets/DA_Balancing_C_Rollbot_Boom.json](../Sources/PioneerGame/Content/Pioneer/Enemies/RollBot/Boom/DataAssets/DA_Balancing_C_Rollbot_Boom.json)
- [Content/Pioneer/Enemies/RollBot/Boom/DataAssets/DA_EnemyMetaData_Rollbot_Boom.json](../Sources/PioneerGame/Content/Pioneer/Enemies/RollBot/Boom/DataAssets/DA_EnemyMetaData_Rollbot_Boom.json)
- [Content/Pioneer/Enemies/RollBot/Boom/DataAssets/DA_EnemyType_Rollbot_Boom.json](../Sources/PioneerGame/Content/Pioneer/Enemies/RollBot/Boom/DataAssets/DA_EnemyType_Rollbot_Boom.json)

</details>
