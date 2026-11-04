# Shredder

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 385 HP. **Internal class:** `C_Runner`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Shredder.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Shredder/01_Original_Materials_B.png"><img src="Renders/Shredder/01_Original_Materials_B.png" width="48%" alt="Shredder: Original Materials"></a>
<a href="Renders/Shredder/03_Part_Health_B.png"><img src="Renders/Shredder/03_Part_Health_B.png" width="48%" alt="Shredder: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Without armor |
| B | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Without armor**

<a href="Renders/Shredder/01_Original_Materials_A.png"><img src="Renders/Shredder/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Shredder/02_Part_Type_A.png"><img src="Renders/Shredder/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Shredder/03_Part_Health_A.png"><img src="Renders/Shredder/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Shredder/04_Break_Off_A.png"><img src="Renders/Shredder/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Shredder/05_Scavenge_Interaction_A.png"><img src="Renders/Shredder/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Shredder/06_Damage_Targets_A.png"><img src="Renders/Shredder/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

**B: Full model**

<a href="Renders/Shredder/01_Original_Materials_B.png"><img src="Renders/Shredder/01_Original_Materials_B.png" width="32%" alt="Original Materials, layer B"></a>
<a href="Renders/Shredder/02_Part_Type_B.png"><img src="Renders/Shredder/02_Part_Type_B.png" width="32%" alt="Part Type, layer B"></a>
<a href="Renders/Shredder/03_Part_Health_B.png"><img src="Renders/Shredder/03_Part_Health_B.png" width="32%" alt="Part Health, layer B"></a>
<a href="Renders/Shredder/04_Break_Off_B.png"><img src="Renders/Shredder/04_Break_Off_B.png" width="32%" alt="Break Off, layer B"></a>
<a href="Renders/Shredder/05_Scavenge_Interaction_B.png"><img src="Renders/Shredder/05_Scavenge_Interaction_B.png" width="32%" alt="Scavenge Interaction, layer B"></a>
<a href="Renders/Shredder/06_Damage_Targets_B.png"><img src="Renders/Shredder/06_Damage_Targets_B.png" width="32%" alt="Damage Targets, layer B"></a>

</details>

### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Thruster_02_C_01_Socket | — | — | — |  |
| Thruster_02_L_01_Socket | — | — | — |  |
| Thruster_02_R_01_Socket | — | — | — |  |
| DummyParent_Root | 385 | Normal | 1 | 0 |
| Body_01 | 385 | Normal | 1 | 0 |
| Armor_01_C | 50 | Armor | 0.4 | 7 |
| Armor_02_L | 50 | Armor | 0.4 | 7 |
| Armor_02_R | 50 | Armor | 0.4 | 7 |
| Hatch_01_C_01 | 38.4 | Armor | 0.4 | 6 |
| HatchHydraulics_01_C_01 | 76.8 | Normal | 1 | 5 |
| Hatch_01_L_01 | 38.4 | Armor | 0.4 | 6 |
| HatchHydraulics_01_L_01 | 76.8 | Normal | 1 | 5 |
| Hatch_01_R_01 | 38.4 | Armor | 0.4 | 6 |
| HatchHydraulics_01_R_01 | 76.8 | Normal | 1 | 5 |
| HatchHydraulics_02_C_01 | 76.8 | Normal | 1 | 5 |
| HatchHydraulics_02_L_01 | 76.8 | Normal | 1 | 5 |
| HatchHydraulics_02_R_01 | 76.8 | Normal | 1 | 5 |
| Thruster_01_C_01 | 10000 | Normal | 1 | 4 |
| Thruster_02_C_01 | 96 | Fragile | 1.2 | 3 |
| Thruster_02_L_01 | 96 | Fragile | 1.2 | 3 |
| Thruster_02_R_01 | 96 | Fragile | 1.2 | 3 |
| Head_01 | 2000 | Armor | 0.4 | 1 |
| Antenna | — | Normal | 1 |  |
| Eye_01 | 2000 | Normal | 1 | 8 |
| Weapon_01 | 1000 | Normal | 1 | 2 |
| VisionConeDummy | — | — | — |  |
| WheelProxy_Back_C_0 | — | — | — |  |
| WheelProxy_Center | — | — | — |  |
| WheelProxy_FrontLeft | — | — | — |  |
| WheelProxy_FrontRight | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ANY(ID.Frame, ID.DummyRoot) | 385 | DummyParent_Root, Body_01 |
| 1 | ID.Head | 2000 | Head_01 |
| 2 | ID.Weapon.Blast | 1000 | Weapon_01 |
| 3 | ID.Thruster.Small | 96 | Thruster_02_C_01, Thruster_02_L_01, Thruster_02_R_01 |
| 4 | ID.Thruster.Big | 10000 | Thruster_01_C_01 |
| 5 | ID.Actuator | 76.8 | HatchHydraulics_01_C_01, HatchHydraulics_01_L_01, HatchHydraulics_01_R_01, HatchHydraulics_02_C_01, HatchHydraulics_02_L_01, HatchHydraulics_02_R_01 |
| 6 | ID.Armor.Medium | 38.4 | Hatch_01_C_01, Hatch_01_L_01, Hatch_01_R_01 |
| 7 | ID.Armor.Heavy | 50 | Armor_01_C, Armor_02_L, Armor_02_R |
| 8 | ID.Eye | 2000 | Eye_01 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Runner/CS_Runner_Skinned.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Runner/CS_Runner_Skinned.json)
- [Content/Pioneer/Enemies/Runner/C_Runner.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Runner/C_Runner.json)
- [Content/Pioneer/Enemies/Runner/Shredder/Art/CSSC_Runner.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Runner/Shredder/Art/CSSC_Runner.json)
- [Content/Pioneer/Enemies/Runner/Shredder/DataAssets/DA_Balancing_C_Runner.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Runner/Shredder/DataAssets/DA_Balancing_C_Runner.json)
- [Content/Pioneer/Enemies/Runner/Shredder/DataAssets/DA_EnemyMetaData_Runner.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Runner/Shredder/DataAssets/DA_EnemyMetaData_Runner.json)
- [Content/Pioneer/Enemies/Runner/Shredder/DataAssets/DA_EnemyType_Runner.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Runner/Shredder/DataAssets/DA_EnemyType_Runner.json)

</details>
