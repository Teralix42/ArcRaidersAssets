# Firefly

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 200 HP. **Internal class:** `C_EliteDrone_Flamethrower`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_Balancing_C_EliteDrone_Flamethrower.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_EnemyType_EliteDrone_Flamethrower.json)

<details>
<summary>More game files</summary>

- [CS_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/CS_EliteDrone_Flamethrower.json)
- [C_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/C_EliteDrone_Flamethrower.json)
- [GA_EliteDrone_Flamethrower_Explosion.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/Capabilities/GA_EliteDrone_Flamethrower_Explosion.json)
- [CSSC_EliteDrone_FlameThrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/CSSC_EliteDrone_FlameThrower.json)
- [DA_EnemyMetaData_EliteDrone_Flamethrower.json](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/DataAssets/DA_EnemyMetaData_EliteDrone_Flamethrower.json)

</details>

[Interactive Blender inspection model](Models/Firefly.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Firefly/01_Original_Materials_C.png"><img src="Renders/Firefly/01_Original_Materials_C.png" width="48%" alt="Firefly: Original Materials"></a>
<a href="Renders/Firefly/03_Part_Health_C.png"><img src="Renders/Firefly/03_Part_Health_C.png" width="48%" alt="Firefly: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Firefly/01_Original_Materials_A.png"><img src="Renders/Firefly/01_Original_Materials_A.png" width="31%" alt="Firefly original materials"></a>
  <a href="Renders/Firefly/01_Original_Materials_B.png"><img src="Renders/Firefly/01_Original_Materials_B.png" width="31%" alt="Firefly original materials"></a>
  <a href="Renders/Firefly/01_Original_Materials_C.png"><img src="Renders/Firefly/01_Original_Materials_C.png" width="31%" alt="Firefly original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Firefly/02_Part_Type_A.png"><img src="Renders/Firefly/02_Part_Type_A.png" width="31%" alt="Firefly part type"></a>
  <a href="Renders/Firefly/02_Part_Type_B.png"><img src="Renders/Firefly/02_Part_Type_B.png" width="31%" alt="Firefly part type"></a>
  <a href="Renders/Firefly/02_Part_Type_C.png"><img src="Renders/Firefly/02_Part_Type_C.png" width="31%" alt="Firefly part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Firefly/03_Part_Health_A.png"><img src="Renders/Firefly/03_Part_Health_A.png" width="31%" alt="Firefly part health"></a>
  <a href="Renders/Firefly/03_Part_Health_B.png"><img src="Renders/Firefly/03_Part_Health_B.png" width="31%" alt="Firefly part health"></a>
  <a href="Renders/Firefly/03_Part_Health_C.png"><img src="Renders/Firefly/03_Part_Health_C.png" width="31%" alt="Firefly part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Firefly/04_Break_Off_A.png"><img src="Renders/Firefly/04_Break_Off_A.png" width="31%" alt="Firefly break-off parts"></a>
  <a href="Renders/Firefly/04_Break_Off_B.png"><img src="Renders/Firefly/04_Break_Off_B.png" width="31%" alt="Firefly break-off parts"></a>
  <a href="Renders/Firefly/04_Break_Off_C.png"><img src="Renders/Firefly/04_Break_Off_C.png" width="31%" alt="Firefly break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Firefly/05_Scavenge_Interaction_A.png"><img src="Renders/Firefly/05_Scavenge_Interaction_A.png" width="31%" alt="Firefly scavenging"></a>
  <a href="Renders/Firefly/05_Scavenge_Interaction_B.png"><img src="Renders/Firefly/05_Scavenge_Interaction_B.png" width="31%" alt="Firefly scavenging"></a>
  <a href="Renders/Firefly/05_Scavenge_Interaction_C.png"><img src="Renders/Firefly/05_Scavenge_Interaction_C.png" width="31%" alt="Firefly scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Firefly/06_Damage_Targets_A.png"><img src="Renders/Firefly/06_Damage_Targets_A.png" width="31%" alt="Firefly damage targets"></a>
  <a href="Renders/Firefly/06_Damage_Targets_B.png"><img src="Renders/Firefly/06_Damage_Targets_B.png" width="31%" alt="Firefly damage targets"></a>
  <a href="Renders/Firefly/06_Damage_Targets_C.png"><img src="Renders/Firefly/06_Damage_Targets_C.png" width="31%" alt="Firefly damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core | 167 | Critical | 1.5 |

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Frame | Blunt | 30 |
| ID.Weapon.Rifle | Blunt | 25 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Barrel_Socket | — | — | — |  |
| Eye_Socket | — | — | — |  |
| Thruster_L_01_Socket | — | — | — |  |
| Thruster_L_02_Socket | — | — | — |  |
| Thruster_R_01_Socket | — | — | — |  |
| Thruster_R_02_Socket | — | — | — |  |
| Frame | 200 | Normal | 1 | 6 |
| Head | 1300 | Fragile | 1.2 | 5 |
| ShieldLower_01 | 64 | Armor | 0.4 | 0 |
| Hatch_L | 6 | Armor | 0.4 | 3 |
| Hatch_R | 6 | Armor | 0.4 | 3 |
| ShieldUpper_01 | 32 | Armor | 0.4 | 1 |
| ShieldWing_L | 32 | Armor | 0.4 | 1 |
| ShieldWing_R | 32 | Armor | 0.4 | 1 |
| Thruster_L_01 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_L_01 | 16 | Armor | 0.4 | 2 |
| Thruster_L_02 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_L_02 | 16 | Armor | 0.4 | 2 |
| Thruster_R_01 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_R_01 | 16 | Armor | 0.4 | 2 |
| Thruster_R_02 | 30 | Fragile | 1.2 | 7 |
| ShieldThruster_R_02 | 16 | Armor | 0.4 | 2 |
| WeaponAttachment | 1000 | Sturdy | 0.4 | 4 |
| Core | 167 | Critical | 1.5 | 9 |
| ShieldCore_01 | 32 | Armor | 0.4 | 1 |
| Weapon | 1000 | Sturdy | 0.4 | 8 |
| EyeDummyPart | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Armor.Body | 64 | ShieldLower_01 |
| 1 | ID.Armor.Heavy | 32 | ShieldUpper_01, ShieldWing_L, ShieldWing_R, ShieldCore_01 |
| 2 | ID.Armor.Medium | 16 | ShieldThruster_L_01, ShieldThruster_L_02, ShieldThruster_R_01, ShieldThruster_R_02 |
| 3 | ID.Armor.Light | 6 | Hatch_L, Hatch_R |
| 4 | ALL(Group.Indestructible, NONE(ID.Weapon.Rifle)) | 1000 | WeaponAttachment |
| 5 | ID.Head | 1300 | Head |
| 6 | ID.Frame | 200 | Frame |
| 7 | ID.Thruster | 30 | Thruster_L_01, Thruster_L_02, Thruster_R_01, Thruster_R_02 |
| 8 | ID.Weapon.Rifle | 1000 | Weapon |
| 9 | ANY(ID.Core) | 167 | Core |

<details>
<summary>Destruction and stun rules</summary>

**Chain destruction**

| Trigger part | Configured threshold | Parts destroyed |
| --- | --- | --- |
| ShieldLower_01 | 1% HP | ShieldWing_L, ShieldWing_R |

**Damage triggers**

| Trigger part | Condition | Effect |
| --- | --- | --- |
| Frame | Part break | [GA_EliteDrone_Flamethrower_Explosion_C](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/Capabilities/GA_EliteDrone_Flamethrower_Explosion.json) |
| Core | 50% HP threshold | [GA_EliteDrone_Flamethrower_Explosion_C](../Sources/PioneerGame/Content/Pioneer/Enemies/EliteDrone/Flamethrower/Capabilities/GA_EliteDrone_Flamethrower_Explosion.json) |

</details>
