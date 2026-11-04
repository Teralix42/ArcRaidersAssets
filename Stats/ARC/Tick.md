# Tick

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 10 HP. **Internal class:** `C_TickBot`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Tick/DA_Balancing_C_TickBot.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Tick/DA_EnemyType_Tick.json)

<details>
<summary>More game files</summary>

- [C_TickBot.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Tick/C_TickBot.json)
- [DA_EnemyMetaData_TickBot.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Tick/DA_EnemyMetaData_TickBot.json)
- [CS_TickBot_01.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Tick/TickBot/CS_TickBot_01.json)

</details>

[Interactive Blender inspection model](Models/Tick.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Tick/01_Original_Materials_A.png"><img src="Renders/Tick/01_Original_Materials_A.png" width="48%" alt="Tick: Original Materials"></a>
<a href="Renders/Tick/03_Part_Health_A.png"><img src="Renders/Tick/03_Part_Health_A.png" width="48%" alt="Tick: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Tick/01_Original_Materials_A.png"><img src="Renders/Tick/01_Original_Materials_A.png" width="48%" alt="Tick original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Tick/02_Part_Type_A.png"><img src="Renders/Tick/02_Part_Type_A.png" width="48%" alt="Tick part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Tick/03_Part_Health_A.png"><img src="Renders/Tick/03_Part_Health_A.png" width="48%" alt="Tick part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Tick/04_Break_Off_A.png"><img src="Renders/Tick/04_Break_Off_A.png" width="48%" alt="Tick break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Tick/05_Scavenge_Interaction_A.png"><img src="Renders/Tick/05_Scavenge_Interaction_A.png" width="48%" alt="Tick scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Tick/06_Damage_Targets_A.png"><img src="Renders/Tick/06_Damage_Targets_A.png" width="48%" alt="Tick damage targets"></a>
</p>

</details>

### Weak and critical parts

No explicit WeakPoint/Critical resistance assignment was recovered for this profile. This does not imply invulnerability.

### Outgoing damage rules

Configured values keyed by the part or attack tag. Attack timing and the final damage against a Raider depend on the attack and target.

| Tag | Damage type | Configured damage |
| --- | --- | --- |
| ID.Leg | Blunt | 5 |
| ID.Frame | Blunt | 2 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| Frame | 10 | — | — | 3 |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Core | 10 |  |
| 1 | ID.Claw | 10 |  |
| 2 | ID.Leg | 10 |  |
| 3 | ID.Frame | 10 | Frame |
| 4 | ID.Armor.Light | 10 |  |
| 5 | Group.Indestructible | 10000 |  |

<details>
<summary>Destruction and stun rules</summary>

**Destruction groups**

| Part query | Destruction damage | Max level | Game file |
| --- | --- | --- | --- |
| ANY(ID.Core) | 100 | 0 | [Actor config](../Sources/PioneerGame/Content/Pioneer/Enemies/Tick/C_TickBot.json) |

</details>
