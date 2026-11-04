# ARC Reclaimer

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 830 HP. **Internal class:** `C_Courier`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Reclaimer.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Reclaimer/01_Original_Materials_A.png"><img src="Renders/Reclaimer/01_Original_Materials_A.png" width="48%" alt="ARC Reclaimer: Original Materials"></a>
<a href="Renders/Reclaimer/03_Part_Health_A.png"><img src="Renders/Reclaimer/03_Part_Health_A.png" width="48%" alt="ARC Reclaimer: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Reclaimer/01_Original_Materials_A.png"><img src="Renders/Reclaimer/01_Original_Materials_A.png" width="48%" alt="Reclaimer original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Reclaimer/02_Part_Type_A.png"><img src="Renders/Reclaimer/02_Part_Type_A.png" width="48%" alt="Reclaimer part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Reclaimer/03_Part_Health_A.png"><img src="Renders/Reclaimer/03_Part_Health_A.png" width="48%" alt="Reclaimer part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Reclaimer/04_Break_Off_A.png"><img src="Renders/Reclaimer/04_Break_Off_A.png" width="48%" alt="Reclaimer break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Reclaimer/05_Scavenge_Interaction_A.png"><img src="Renders/Reclaimer/05_Scavenge_Interaction_A.png" width="48%" alt="Reclaimer scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Reclaimer/06_Damage_Targets_A.png"><img src="Renders/Reclaimer/06_Damage_Targets_A.png" width="48%" alt="Reclaimer damage targets"></a>
</p>

</details>

### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| ScannerSocket | — | — | — |  |
| SmallThruster_01 | — | — | — |  |
| SmallThruster_02 | — | — | — |  |
| SmallThruster_03 | — | — | — |  |
| Main | 830 | Sturdy | 0.4 | 0 |
| Hatch_01 | 10000 | Sturdy | 0.4 | 2 |
| Thruster_C_01 | 350 | Sturdy | 0.4 | 1 |
| Thruster_L_02 | 350 | Sturdy | 0.4 | 1 |
| Thruster_R_02 | 350 | Sturdy | 0.4 | 1 |
| ScannerStyle | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ANY(ID.Frame) | 830 | Main |
| 1 | ANY(ID.Thruster) | 350 | Thruster_C_01, Thruster_L_02, Thruster_R_02 |
| 2 | ANY(ID.Armor.Heavy) | 10000 | Hatch_01 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/Courier/Art/CSSC_Courier.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/Art/CSSC_Courier.json)
- [Content/Pioneer/Enemies/Courier/CS_Courier.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/CS_Courier.json)
- [Content/Pioneer/Enemies/Courier/C_Courier.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/C_Courier.json)
- [Content/Pioneer/Enemies/Courier/Capabilities/GA_ShoveOffFrigate.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/Capabilities/GA_ShoveOffFrigate.json)
- [Content/Pioneer/Enemies/Courier/DataAssets/DA_Balancing_C_Courier.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/DataAssets/DA_Balancing_C_Courier.json)
- [Content/Pioneer/Enemies/Courier/DataAssets/DA_EnemyMetaData_Courier.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/DataAssets/DA_EnemyMetaData_Courier.json)
- [Content/Pioneer/Enemies/Courier/DataAssets/DA_EnemyType_Courier.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Courier/DataAssets/DA_EnemyType_Courier.json)

</details>
