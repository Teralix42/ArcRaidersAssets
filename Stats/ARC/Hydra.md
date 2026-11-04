# Hydra

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 1050 HP. **Internal class:** `C_Kebab_Gatling`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_Balancing_C_Kebab_Gatling.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_EnemyType_Kebab_Gatling.json)

<details>
<summary>More game files</summary>

- [CSSC_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/Art/CSSC_Kebab_Gatling.json)
- [C_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/C_Kebab_Gatling.json)
- [DA_EnemyMetaData_Kebab_Gatling.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Kebab/Gatling/DataAssets/DA_EnemyMetaData_Kebab_Gatling.json)

</details>

[Interactive Blender inspection model](Models/Hydra.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Hydra/01_Original_Materials_C.png"><img src="Renders/Hydra/01_Original_Materials_C.png" width="48%" alt="Hydra: Original Materials"></a>
<a href="Renders/Hydra/03_Part_Health_C.png"><img src="Renders/Hydra/03_Part_Health_C.png" width="48%" alt="Hydra: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Hydra/01_Original_Materials_A.png"><img src="Renders/Hydra/01_Original_Materials_A.png" width="31%" alt="Hydra original materials"></a>
  <a href="Renders/Hydra/01_Original_Materials_B.png"><img src="Renders/Hydra/01_Original_Materials_B.png" width="31%" alt="Hydra original materials"></a>
  <a href="Renders/Hydra/01_Original_Materials_C.png"><img src="Renders/Hydra/01_Original_Materials_C.png" width="31%" alt="Hydra original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Hydra/02_Part_Type_A.png"><img src="Renders/Hydra/02_Part_Type_A.png" width="31%" alt="Hydra part type"></a>
  <a href="Renders/Hydra/02_Part_Type_B.png"><img src="Renders/Hydra/02_Part_Type_B.png" width="31%" alt="Hydra part type"></a>
  <a href="Renders/Hydra/02_Part_Type_C.png"><img src="Renders/Hydra/02_Part_Type_C.png" width="31%" alt="Hydra part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Hydra/03_Part_Health_A.png"><img src="Renders/Hydra/03_Part_Health_A.png" width="31%" alt="Hydra part health"></a>
  <a href="Renders/Hydra/03_Part_Health_B.png"><img src="Renders/Hydra/03_Part_Health_B.png" width="31%" alt="Hydra part health"></a>
  <a href="Renders/Hydra/03_Part_Health_C.png"><img src="Renders/Hydra/03_Part_Health_C.png" width="31%" alt="Hydra part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Hydra/04_Break_Off_A.png"><img src="Renders/Hydra/04_Break_Off_A.png" width="31%" alt="Hydra break-off parts"></a>
  <a href="Renders/Hydra/04_Break_Off_B.png"><img src="Renders/Hydra/04_Break_Off_B.png" width="31%" alt="Hydra break-off parts"></a>
  <a href="Renders/Hydra/04_Break_Off_C.png"><img src="Renders/Hydra/04_Break_Off_C.png" width="31%" alt="Hydra break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Hydra/05_Scavenge_Interaction_A.png"><img src="Renders/Hydra/05_Scavenge_Interaction_A.png" width="31%" alt="Hydra scavenging"></a>
  <a href="Renders/Hydra/05_Scavenge_Interaction_B.png"><img src="Renders/Hydra/05_Scavenge_Interaction_B.png" width="31%" alt="Hydra scavenging"></a>
  <a href="Renders/Hydra/05_Scavenge_Interaction_C.png"><img src="Renders/Hydra/05_Scavenge_Interaction_C.png" width="31%" alt="Hydra scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Hydra/06_Damage_Targets_A.png"><img src="Renders/Hydra/06_Damage_Targets_A.png" width="31%" alt="Hydra damage targets"></a>
  <a href="Renders/Hydra/06_Damage_Targets_B.png"><img src="Renders/Hydra/06_Damage_Targets_B.png" width="31%" alt="Hydra damage targets"></a>
  <a href="Renders/Hydra/06_Damage_Targets_C.png"><img src="Renders/Hydra/06_Damage_Targets_C.png" width="31%" alt="Hydra damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Weakpoint_01 | 800 | WeakPoint | 1.5 |
| Weakpoint_02 | 800 | WeakPoint | 1.5 |
| Weakpoint_03 | 800 | WeakPoint | 1.5 |

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Segment | Blunt | 1.5 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| GunTop_L_01_Muzzle | 280 | — | — | 3 |
| GunTop_R_01_Muzzle | 280 | — | — | 3 |
| GunMid_L_01_Muzzle | 280 | — | — | 3 |
| GunMid_R_01_Muzzle | 280 | — | — | 3 |
| GunBot_L_01_Muzzle | 280 | — | — | 3 |
| GunBot_R_01_Muzzle | 280 | — | — | 3 |
| Turret_01_Laser | — | — | — |  |
| Turret_02_Laser | — | — | — |  |
| Turret_03_Laser | — | — | — |  |
| DummyFrame | 9999 | Sturdy | 0.4 | 5 |
| Frame_01 | 1050 | Sturdy | 0.4 | 0 |
| CenterAxis_01 | 9999 | Sturdy | 0.4 | 5 |
| Head_01 | 9999 | Sturdy | 0.4 | 5 |
| Turret_01 | 550 | Sturdy | 0.4 | 1 |
| Armor_01 | 100 | Armor | 0.4 | 4 |
| GunTop_L_01 | 280 | Sturdy | 0.4 | 3 |
| GunTop_R_01 | 280 | Sturdy | 0.4 | 3 |
| Weakpoint_01 | 800 | WeakPoint | 1.5 | 2 |
| Turret_02 | 550 | Sturdy | 0.4 | 1 |
| Armor_02 | 100 | Armor | 0.4 | 4 |
| GunMid_L_01 | 280 | Sturdy | 0.4 | 3 |
| GunMid_R_01 | 280 | Sturdy | 0.4 | 3 |
| Weakpoint_02 | 800 | WeakPoint | 1.5 | 2 |
| Turret_03 | 550 | Sturdy | 0.4 | 1 |
| Armor_03 | 100 | Armor | 0.4 | 4 |
| GunBot_L_01 | 280 | Sturdy | 0.4 | 3 |
| GunBot_R_01 | 280 | Sturdy | 0.4 | 3 |
| Weakpoint_03 | 800 | WeakPoint | 1.5 | 2 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ANY(ID.Frame) | 1050 | Frame_01 |
| 1 | ANY(ID.Joint) | 550 | Turret_01, Turret_02, Turret_03 |
| 2 | ANY(ID.Core) | 800 | Weakpoint_01, Weakpoint_02, Weakpoint_03 |
| 3 | ANY(ID.Weapon.GatlingGun) | 280 | GunTop_L_01_Muzzle, GunTop_R_01_Muzzle, GunMid_L_01_Muzzle, GunMid_R_01_Muzzle, GunBot_L_01_Muzzle, GunBot_R_01_Muzzle, GunTop_L_01, GunTop_R_01, GunMid_L_01, GunMid_R_01, GunBot_L_01, GunBot_R_01 |
| 4 | ID.Armor | 100 | Armor_01, Armor_02, Armor_03 |
| 5 | ANY(ID.DummyRoot, Group.Indestructible) | 9999 | DummyFrame, CenterAxis_01, Head_01 |

<details>
<summary>Destruction and stun rules</summary>

**Chain destruction**

| Trigger part | Configured threshold | Parts destroyed |
| --- | --- | --- |
| Turret_01, Turret_02, Turret_03 | 1% HP | Frame_01 |

**Stun propagation**

| Source part query | Destination part query |
| --- | --- |
| ID.Segment.Top | ID.Segment.Top |
| ID.Segment.Middle | ID.Segment.Middle |
| ID.Segment.Bottom | ID.Segment.Bottom |

</details>
