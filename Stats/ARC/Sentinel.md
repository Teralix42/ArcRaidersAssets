# Sentinel

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 300 HP. **Internal class:** `C_Sniper`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Sentinel.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Sentinel/01_Original_Materials_A.png"><img src="Renders/Sentinel/01_Original_Materials_A.png" width="48%" alt="Sentinel: Original Materials"></a>
<a href="Renders/Sentinel/03_Part_Health_A.png"><img src="Renders/Sentinel/03_Part_Health_A.png" width="48%" alt="Sentinel: Part Health"></a>

### Layers and views

| Layer | Visible structure |
| --- | --- |
| A | Full model |

<details>
<summary>All six views, including inner layers</summary>


**A: Full model**

<a href="Renders/Sentinel/01_Original_Materials_A.png"><img src="Renders/Sentinel/01_Original_Materials_A.png" width="32%" alt="Original Materials, layer A"></a>
<a href="Renders/Sentinel/02_Part_Type_A.png"><img src="Renders/Sentinel/02_Part_Type_A.png" width="32%" alt="Part Type, layer A"></a>
<a href="Renders/Sentinel/03_Part_Health_A.png"><img src="Renders/Sentinel/03_Part_Health_A.png" width="32%" alt="Part Health, layer A"></a>
<a href="Renders/Sentinel/04_Break_Off_A.png"><img src="Renders/Sentinel/04_Break_Off_A.png" width="32%" alt="Break Off, layer A"></a>
<a href="Renders/Sentinel/05_Scavenge_Interaction_A.png"><img src="Renders/Sentinel/05_Scavenge_Interaction_A.png" width="32%" alt="Scavenge Interaction, layer A"></a>
<a href="Renders/Sentinel/06_Damage_Targets_A.png"><img src="Renders/Sentinel/06_Damage_Targets_A.png" width="32%" alt="Damage Targets, layer A"></a>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Weakpoint | 225 | WeakPoint | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Muzzle | — | — | — |  |
| Laser | — | — | — |  |
| Body | 300 | Normal | 1 | 1 |
| ArmPivot | 300 | Normal | 1 | 1 |
| Arm | 300 | Normal | 1 | 1 |
| HeadOrienter | 300 | Normal | 1 | 1 |
| Head | 300 | Normal | 1 | 1 |
| Barrel | 300 | Normal | 1 | 0 |
| Weakpoint | 225 | WeakPoint | 1.5 | 2 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Weapon | 300 | Barrel |
| 1 | ANY(ID.Frame, ID.Head, ID.Arm, Group.Indestructible) | 300 | Body, ArmPivot, Arm, HeadOrienter, Head |
| 2 | Group.Weakpoint | 225 | Weakpoint |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Sniper/CSSC_Sniper.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Sniper/CSSC_Sniper.json)
- [Content/Pioneer/Enemies/Sniper/C_Sniper.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Sniper/C_Sniper.json)
- [Content/Pioneer/Enemies/Sniper/DataAssets/DA_Balancing_C_Sniper.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Sniper/DataAssets/DA_Balancing_C_Sniper.json)
- [Content/Pioneer/Enemies/Sniper/DataAssets/DA_EnemyMetaData_Sniper.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Sniper/DataAssets/DA_EnemyMetaData_Sniper.json)
- [Content/Pioneer/Enemies/Sniper/DataAssets/DA_EnemyType_Sniper.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Sniper/DataAssets/DA_EnemyType_Sniper.json)

</details>
