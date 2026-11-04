# Wasp

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 110 HP. **Internal class:** `C_LightDrone_02`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/LightDrone/Wasp/DA_Balancing_C_LightDrone_02.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/LightDrone/Wasp/DA_EnemyType_LightDrone_02.json)

<details>
<summary>More game files</summary>

- [CSSC_LightDrone_02_SK.json](../Sources/PioneerGame/Content/Pioneer/Enemies/LightDrone/Wasp/CSSC_LightDrone_02_SK.json)
- [CS_LightDrone_02_SK.json](../Sources/PioneerGame/Content/Pioneer/Enemies/LightDrone/Wasp/CS_LightDrone_02_SK.json)
- [C_LightDrone_02.json](../Sources/PioneerGame/Content/Pioneer/Enemies/LightDrone/Wasp/C_LightDrone_02.json)
- [DA_EnemyMetaData_LightDrone_02.json](../Sources/PioneerGame/Content/Pioneer/Enemies/LightDrone/Wasp/DA_EnemyMetaData_LightDrone_02.json)

</details>

[Interactive Blender inspection model](Models/Wasp.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Wasp/01_Original_Materials_B.png"><img src="Renders/Wasp/01_Original_Materials_B.png" width="48%" alt="Wasp: Original Materials"></a>
<a href="Renders/Wasp/03_Part_Health_B.png"><img src="Renders/Wasp/03_Part_Health_B.png" width="48%" alt="Wasp: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Wasp/01_Original_Materials_A.png"><img src="Renders/Wasp/01_Original_Materials_A.png" width="47%" alt="Wasp original materials"></a>
  <a href="Renders/Wasp/01_Original_Materials_B.png"><img src="Renders/Wasp/01_Original_Materials_B.png" width="47%" alt="Wasp original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Wasp/02_Part_Type_A.png"><img src="Renders/Wasp/02_Part_Type_A.png" width="47%" alt="Wasp part type"></a>
  <a href="Renders/Wasp/02_Part_Type_B.png"><img src="Renders/Wasp/02_Part_Type_B.png" width="47%" alt="Wasp part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Wasp/03_Part_Health_A.png"><img src="Renders/Wasp/03_Part_Health_A.png" width="47%" alt="Wasp part health"></a>
  <a href="Renders/Wasp/03_Part_Health_B.png"><img src="Renders/Wasp/03_Part_Health_B.png" width="47%" alt="Wasp part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Wasp/04_Break_Off_A.png"><img src="Renders/Wasp/04_Break_Off_A.png" width="47%" alt="Wasp break-off parts"></a>
  <a href="Renders/Wasp/04_Break_Off_B.png"><img src="Renders/Wasp/04_Break_Off_B.png" width="47%" alt="Wasp break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Wasp/05_Scavenge_Interaction_A.png"><img src="Renders/Wasp/05_Scavenge_Interaction_A.png" width="47%" alt="Wasp scavenging"></a>
  <a href="Renders/Wasp/05_Scavenge_Interaction_B.png"><img src="Renders/Wasp/05_Scavenge_Interaction_B.png" width="47%" alt="Wasp scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Wasp/06_Damage_Targets_A.png"><img src="Renders/Wasp/06_Damage_Targets_A.png" width="47%" alt="Wasp damage targets"></a>
  <a href="Renders/Wasp/06_Damage_Targets_B.png"><img src="Renders/Wasp/06_Damage_Targets_B.png" width="47%" alt="Wasp damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Core_01 | 1300 | Critical | 1.5 |

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Weapon | Blunt | 2.5 |
| Group.Explosive | Blunt | 30 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Thruster_L_01_Socket | — | — | — |  |
| Thruster_L_02_Socket | — | — | — |  |
| Thruster_R_01_Socket | — | — | — |  |
| Thruster_R_02_Socket | — | — | — |  |
| Weapon_R_01_Muzzle_Socket | — | — | — |  |
| Weapon_L_01_Muzzle_Socket | — | — | — |  |
| Weapon_L_01_ShellEject_Socket | — | — | — |  |
| Weapon_R_01_ShellEject_Socket | — | — | — |  |
| Frame_01 | 110 | Normal | 1 | 3 |
| Armor_Side_L_01 | 100 | Normal | 1 | 8 |
| Armor_Side_R_01 | 100 | Normal | 1 | 8 |
| Core_01 | 1300 | Critical | 1.5 | 5 |
| Head_01 | 1000 | Fragile | 1.2 | 7 |
| Thruster_L_01 | 30 | Fragile | 1.2 | 4 |
| Thruster_L_02 | 30 | Fragile | 1.2 | 4 |
| Thruster_R_01 | 30 | Fragile | 1.2 | 4 |
| Thruster_R_02 | 30 | Fragile | 1.2 | 4 |
| Weapon_LightRifle_L_01 | 1000 | Sturdy | 0.4 | 1 |
| Weapon_LightRifle_R_01 | 1000 | Sturdy | 0.4 | 1 |
| EyeProxy | — | — | — |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Armor.Light | 10 |  |
| 1 | ID.Weapon | 1000 | Weapon_LightRifle_L_01, Weapon_LightRifle_R_01 |
| 2 | Group.Explosive | 0 |  |
| 3 | ID.Frame | 110 | Frame_01 |
| 4 | ID.Thruster | 30 | Thruster_L_01, Thruster_L_02, Thruster_R_01, Thruster_R_02 |
| 5 | Group.Weakpoint | 1300 | Core_01 |
| 6 | Group.Critical | 1300 |  |
| 7 | ID.Head | 1000 | Head_01 |
| 8 | ID.Armor | 100 | Armor_Side_L_01, Armor_Side_R_01 |
| 9 | HealthGroup.Base | 1000 |  |
