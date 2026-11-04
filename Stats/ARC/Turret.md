# Turret

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 80 HP. **Internal class:** `C_TurretEnemy`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/TurretEnemy/DA_Balancing_C_TurretEnemy.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/TurretEnemy/DA_EnemyType_TurretEnemy.json)

<details>
<summary>More game files</summary>

- [DA_EnemyMetaData_Turret.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Enemies_Archive/Turrets/DA_EnemyMetaData_Turret.json)
- [CSSC_TurretEnemy.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/TurretEnemy/CSSC_TurretEnemy.json)
- [CS_TurretEnemy_SK.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/TurretEnemy/CS_TurretEnemy_SK.json)
- [C_TurretEnemy.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Turret/TurretEnemy/C_TurretEnemy.json)

</details>

[Interactive Blender inspection model](Models/Turret.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Turret/01_Original_Materials_A.png"><img src="Renders/Turret/01_Original_Materials_A.png" width="48%" alt="Turret: Original Materials"></a>
<a href="Renders/Turret/03_Part_Health_A.png"><img src="Renders/Turret/03_Part_Health_A.png" width="48%" alt="Turret: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Turret/01_Original_Materials_A.png"><img src="Renders/Turret/01_Original_Materials_A.png" width="48%" alt="Turret original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Turret/02_Part_Type_A.png"><img src="Renders/Turret/02_Part_Type_A.png" width="48%" alt="Turret part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Turret/03_Part_Health_A.png"><img src="Renders/Turret/03_Part_Health_A.png" width="48%" alt="Turret part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Turret/04_Break_Off_A.png"><img src="Renders/Turret/04_Break_Off_A.png" width="48%" alt="Turret break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Turret/05_Scavenge_Interaction_A.png"><img src="Renders/Turret/05_Scavenge_Interaction_A.png" width="48%" alt="Turret scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Turret/06_Damage_Targets_A.png"><img src="Renders/Turret/06_Damage_Targets_A.png" width="48%" alt="Turret damage targets"></a>
</p>

</details>

### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Turret | Blunt | 2.5 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Body_01 | 80 | Normal | 1 | 0 |
| Head_01 | 80 | Normal | 1 | 1 |
| Arm_01 | 80 | Normal | 1 | 2 |
| Laser | — | Normal | 1 |  |
| MuzzleProxy | — | Normal | 1 |  |
| StaticMeshStyle_SM_Turret_01_GroundPlanes_A | 80 | — | — | 3 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 80 | Body_01 |
| 1 | ID.Head | 80 | Head_01 |
| 2 | ID.Turret | 80 | Arm_01 |
| 3 | ID.GroundMounting | 80 | StaticMeshStyle_SM_Turret_01_GroundPlanes_A |
