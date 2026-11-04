# Spotter

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 80 HP. **Internal class:** `C_Pinger`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Spotter.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Spotter/01_Original_Materials_A.png"><img src="Renders/Spotter/01_Original_Materials_A.png" width="48%" alt="Spotter: Original Materials"></a>
<a href="Renders/Spotter/03_Part_Health_A.png"><img src="Renders/Spotter/03_Part_Health_A.png" width="48%" alt="Spotter: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Full model**

<a href="Renders/Spotter/01_Original_Materials_A.png"><img src="Renders/Spotter/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Spotter/02_Part_Type_A.png"><img src="Renders/Spotter/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Spotter/03_Part_Health_A.png"><img src="Renders/Spotter/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Spotter/04_Break_Off_A.png"><img src="Renders/Spotter/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Spotter/05_Scavenge_Interaction_A.png"><img src="Renders/Spotter/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Spotter/06_Damage_Targets_A.png"><img src="Renders/Spotter/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Head_01 | 120 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Laser | — | — | — |  |
| Frame_01 | 80 | Normal | 1 | 0 |
| Head_01 | 120 | Critical | 1.5 | 2 |
| Ring_C_01 | 120 | Normal | 1 | 3 |
| ScannerRoot | 180 | Normal | 1 | 1 |
| Thruster_L_01 | — | Fragile | 1.2 |  |
| Thruster_L_02 | — | Fragile | 1.2 |  |
| Thruster_R_01 | — | Fragile | 1.2 |  |
| Thruster_R_02 | — | Fragile | 1.2 |  |
| Thruster_Virtual_L_01 | — | Fragile | 1.2 |  |
| Thruster_Virtual_L_02 | — | Fragile | 1.2 |  |
| Thruster_Virtual_R_01 | — | Fragile | 1.2 |  |
| Thruster_Virtual_R_02 | — | Fragile | 1.2 |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 80 | Frame_01 |
| 1 | ID.Radar | 180 | ScannerRoot |
| 2 | ID.Head | 120 | Head_01 |
| 3 | ANY(HealthGroup.Base) | 120 | Ring_C_01 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Pinger/C_Pinger.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pinger/C_Pinger.json)
- [Content/Pioneer/Enemies/Pinger/DataAssets/CSSC_Pinger.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pinger/DataAssets/CSSC_Pinger.json)
- [Content/Pioneer/Enemies/Pinger/DataAssets/DA_Balancing_C_Pinger.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pinger/DataAssets/DA_Balancing_C_Pinger.json)
- [Content/Pioneer/Enemies/Pinger/DataAssets/DA_EnemyMetaData_Pinger.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pinger/DataAssets/DA_EnemyMetaData_Pinger.json)
- [Content/Pioneer/Enemies/Pinger/DataAssets/DA_EnemyType_Pinger.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pinger/DataAssets/DA_EnemyType_Pinger.json)

</details>
