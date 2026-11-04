# Rocketeer

[ARC stats](README.md) · [Machine-readable data](arc_parts.json) · [Damage model](Damage_Model.md)

**Configured frame rule:** 1100 HP. **Internal class:** `C_HeavyDrone_Missile`.

Frame HP is a balancing rule, not the sum of every limb or plate. Part rules and damage propagation are separate. `—` means unknown or unassigned.

[Interactive Blender inspection model](Models/Rocketeer.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Rocketeer/01_Original_Materials_C.png"><img src="Renders/Rocketeer/01_Original_Materials_C.png" width="48%" alt="Rocketeer: Original Materials"></a>
<a href="Renders/Rocketeer/03_Part_Health_C.png"><img src="Renders/Rocketeer/03_Part_Health_C.png" width="48%" alt="Rocketeer: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Rocketeer/01_Original_Materials_A.png"><img src="Renders/Rocketeer/01_Original_Materials_A.png" width="31%" alt="Rocketeer original materials"></a>
  <a href="Renders/Rocketeer/01_Original_Materials_B.png"><img src="Renders/Rocketeer/01_Original_Materials_B.png" width="31%" alt="Rocketeer original materials"></a>
  <a href="Renders/Rocketeer/01_Original_Materials_C.png"><img src="Renders/Rocketeer/01_Original_Materials_C.png" width="31%" alt="Rocketeer original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Rocketeer/02_Part_Type_A.png"><img src="Renders/Rocketeer/02_Part_Type_A.png" width="31%" alt="Rocketeer part type"></a>
  <a href="Renders/Rocketeer/02_Part_Type_B.png"><img src="Renders/Rocketeer/02_Part_Type_B.png" width="31%" alt="Rocketeer part type"></a>
  <a href="Renders/Rocketeer/02_Part_Type_C.png"><img src="Renders/Rocketeer/02_Part_Type_C.png" width="31%" alt="Rocketeer part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Rocketeer/03_Part_Health_A.png"><img src="Renders/Rocketeer/03_Part_Health_A.png" width="31%" alt="Rocketeer part health"></a>
  <a href="Renders/Rocketeer/03_Part_Health_B.png"><img src="Renders/Rocketeer/03_Part_Health_B.png" width="31%" alt="Rocketeer part health"></a>
  <a href="Renders/Rocketeer/03_Part_Health_C.png"><img src="Renders/Rocketeer/03_Part_Health_C.png" width="31%" alt="Rocketeer part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Rocketeer/04_Break_Off_A.png"><img src="Renders/Rocketeer/04_Break_Off_A.png" width="31%" alt="Rocketeer break-off parts"></a>
  <a href="Renders/Rocketeer/04_Break_Off_B.png"><img src="Renders/Rocketeer/04_Break_Off_B.png" width="31%" alt="Rocketeer break-off parts"></a>
  <a href="Renders/Rocketeer/04_Break_Off_C.png"><img src="Renders/Rocketeer/04_Break_Off_C.png" width="31%" alt="Rocketeer break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Rocketeer/05_Scavenge_Interaction_A.png"><img src="Renders/Rocketeer/05_Scavenge_Interaction_A.png" width="31%" alt="Rocketeer scavenging"></a>
  <a href="Renders/Rocketeer/05_Scavenge_Interaction_B.png"><img src="Renders/Rocketeer/05_Scavenge_Interaction_B.png" width="31%" alt="Rocketeer scavenging"></a>
  <a href="Renders/Rocketeer/05_Scavenge_Interaction_C.png"><img src="Renders/Rocketeer/05_Scavenge_Interaction_C.png" width="31%" alt="Rocketeer scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Rocketeer/06_Damage_Targets_A.png"><img src="Renders/Rocketeer/06_Damage_Targets_A.png" width="31%" alt="Rocketeer damage targets"></a>
  <a href="Renders/Rocketeer/06_Damage_Targets_B.png"><img src="Renders/Rocketeer/06_Damage_Targets_B.png" width="31%" alt="Rocketeer damage targets"></a>
  <a href="Renders/Rocketeer/06_Damage_Targets_C.png"><img src="Renders/Rocketeer/06_Damage_Targets_C.png" width="31%" alt="Rocketeer damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core_01 | 2600 | Critical | 1.5 |

### Every named part

These records also include sockets, bones, and proxy components; they are not all independent damageable hitboxes. The weapon’s separate ARC armor and weak-point multipliers still apply where indicated in JSON.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Thruster_L_01_Socket | — | — | — |  |
| Thruster_L_02_Socket | — | — | — |  |
| Thruster_R_01_Socket | — | — | — |  |
| Thruster_R_02_Socket | — | — | — |  |
| Muzzle | — | — | — |  |
| Frame | 1100 | Normal | 1 | 0 |
| Core_01 | 2600 | Critical | 1.5 | 7 |
| Eye_01 | 2600 | Fragile | 1.2 | 7 |
| HeavyDrone_01_Missile_Armor_C_01 | 96 | Armor | 0.4 | 3 |
| HeavyDrone_01_Missile_Hatch_L_01_A | 12 | Armor | 0.4 | 1 |
| HeavyDrone_01_Missile_Hatch_R_01_A | 12 | Armor | 0.4 | 1 |
| HeavyDrone_01_Missile_Armor_L_03 | 96 | Armor | 0.4 | 3 |
| HeavyDrone_01_Missile_Flap_L_01 | 24 | Armor | 0.4 | 2 |
| HeavyDrone_01_Missile_Armor_R_03 | 96 | Armor | 0.4 | 3 |
| HeavyDrone_01_Missile_Flap_R_01 | 24 | Armor | 0.4 | 2 |
| HeavyDrone_01_Missile_Flap_C_01 | 24 | Armor | 0.4 | 2 |
| HeavyDrone_01_Missile_Weapon_Arm_C_01 | 2000 | Sturdy | 0.4 | 6 |
| HeavyDrone_01_Missile_Weapon_Body_01 | 2000 | Sturdy | 0.4 | 5 |
| HeavyDrone_01_Missile_Weapon_Arm_L_01_A | 2000 | Sturdy | 0.4 | 6 |
| HeavyDrone_01_Missile_Weapon_Launcher_L_01 | 2000 | Sturdy | 0.4 | 6 |
| HeavyDrone_01_Missile_Weapon_Arm_R_01_A | 2000 | Sturdy | 0.4 | 6 |
| HeavyDrone_01_Missile_Weapon_Launcher_R_01 | 2000 | Sturdy | 0.4 | 6 |
| Thruster_L_01 | 345 | Fragile | 1.2 | 4 |
| ThrusterArmor_01 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_02 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_03 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_04 | 24 | Armor | 0.4 | 2 |
| Thruster_L_02 | 345 | Fragile | 1.2 | 4 |
| ThrusterArmor_05 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_06 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_07 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_08 | 24 | Armor | 0.4 | 2 |
| Thruster_R_01 | 345 | Fragile | 1.2 | 4 |
| ThrusterArmor_09 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_10 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_11 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_12 | 24 | Armor | 0.4 | 2 |
| Thruster_R_02 | 345 | Fragile | 1.2 | 4 |
| ThrusterArmor_13 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_14 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_15 | 24 | Armor | 0.4 | 2 |
| ThrusterArmor_16 | 24 | Armor | 0.4 | 2 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 1100 | Frame |
| 1 | ID.Armor.Light | 12 | HeavyDrone_01_Missile_Hatch_L_01_A, HeavyDrone_01_Missile_Hatch_R_01_A |
| 2 | ID.Armor.Medium | 24 | HeavyDrone_01_Missile_Flap_L_01, HeavyDrone_01_Missile_Flap_R_01, HeavyDrone_01_Missile_Flap_C_01, ThrusterArmor_01, ThrusterArmor_02, ThrusterArmor_03, ThrusterArmor_04, ThrusterArmor_05, ThrusterArmor_06, ThrusterArmor_07, ThrusterArmor_08, ThrusterArmor_09, ThrusterArmor_10, ThrusterArmor_11, ThrusterArmor_12, ThrusterArmor_13, ThrusterArmor_14, ThrusterArmor_15, ThrusterArmor_16 |
| 3 | ID.Armor.Heavy | 96 | HeavyDrone_01_Missile_Armor_C_01, HeavyDrone_01_Missile_Armor_L_03, HeavyDrone_01_Missile_Armor_R_03 |
| 4 | ID.Thruster | 345 | Thruster_L_01, Thruster_L_02, Thruster_R_01, Thruster_R_02 |
| 5 | ID.Weapon.Missile | 2000 | HeavyDrone_01_Missile_Weapon_Body_01 |
| 6 | ALL(Group.Indestructible, NONE(ID.Weapon.Missile)) | 2000 | HeavyDrone_01_Missile_Weapon_Arm_C_01, HeavyDrone_01_Missile_Weapon_Arm_L_01_A, HeavyDrone_01_Missile_Weapon_Launcher_L_01, HeavyDrone_01_Missile_Weapon_Arm_R_01_A, HeavyDrone_01_Missile_Weapon_Launcher_R_01 |
| 7 | Group.Critical | 2600 | Core_01, Eye_01 |

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/Art/SK/CSSC_HeavyDroneMissile.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/Art/SK/CSSC_HeavyDroneMissile.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/C_HeavyDrone_Missile.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/C_HeavyDrone_Missile.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/DataAssets/DA_Balancing_C_HeavyDrone_Missile.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/DataAssets/DA_Balancing_C_HeavyDrone_Missile.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/DataAssets/DA_EnemyMetaData_HeavyDroneMissile.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/DataAssets/DA_EnemyMetaData_HeavyDroneMissile.json)
- [Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/DataAssets/DA_EnemyType_HeavyDroneMissile.json](../Sources/PioneerGame/Content/Pioneer/Enemies/HeavyDrone/HeavyDroneMissile/DataAssets/DA_EnemyType_HeavyDroneMissile.json)

</details>
