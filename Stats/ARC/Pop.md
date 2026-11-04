# Pop

[ARC stats](README.md) · [Damage model](Damage_Model.md)

**Configured frame rule:** 20 HP. **Internal class:** `C_RollBot_Pop`.

Frame HP is assigned separately from part HP. A dash marks an unknown or unassigned value.

[Balancing and part HP](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/DataAssets/DA_Balancing_C_RollBot_Pop.json) · [Enemy type](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/DataAssets/DA_EnemyType_RollBot_Pop.json)

<details>
<summary>More game files</summary>

- [C_RollBot_Pop.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/C_RollBot_Pop.json)
- [CSSC_RollBot_Pop.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/DataAssets/CSSC_RollBot_Pop.json)
- [DA_EnemyMetaData_RollBot_Pop.json](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/DataAssets/DA_EnemyMetaData_RollBot_Pop.json)

</details>

[Interactive Blender inspection model](Models/Pop.blend) · Native textures and inspector are packed into the file.

<a href="Renders/Pop/01_Original_Materials_A.png"><img src="Renders/Pop/01_Original_Materials_A.png" width="48%" alt="Pop: Original Materials"></a>
<a href="Renders/Pop/03_Part_Health_A.png"><img src="Renders/Pop/03_Part_Health_A.png" width="48%" alt="Pop: Part Health"></a>

<details>
<summary>All stat renders</summary>

**Original materials**

<p align="center">
  <a href="Renders/Pop/01_Original_Materials_A.png"><img src="Renders/Pop/01_Original_Materials_A.png" width="48%" alt="Pop original materials"></a>
</p>

**Part type**

<p align="center">
  <a href="Renders/Pop/02_Part_Type_A.png"><img src="Renders/Pop/02_Part_Type_A.png" width="48%" alt="Pop part type"></a>
</p>

**Part health**

<p align="center">
  <a href="Renders/Pop/03_Part_Health_A.png"><img src="Renders/Pop/03_Part_Health_A.png" width="48%" alt="Pop part health"></a>
</p>

**Break-off parts**

<p align="center">
  <a href="Renders/Pop/04_Break_Off_A.png"><img src="Renders/Pop/04_Break_Off_A.png" width="48%" alt="Pop break-off parts"></a>
</p>

**Scavenging**

<p align="center">
  <a href="Renders/Pop/05_Scavenge_Interaction_A.png"><img src="Renders/Pop/05_Scavenge_Interaction_A.png" width="48%" alt="Pop scavenging"></a>
</p>

**Damage targets**

<p align="center">
  <a href="Renders/Pop/06_Damage_Targets_A.png"><img src="Renders/Pop/06_Damage_Targets_A.png" width="48%" alt="Pop damage targets"></a>
</p>

</details>

### Weak and critical parts

| Part | Configured HP | Group | Baseline physical damage × |
| --- | --- | --- | --- |
| Frame_01 | 20 | Critical | 1.5 |

### Every named part

This list includes mesh records such as sockets and proxies. See the [damage model](Damage_Model.md) for how weapon multipliers apply to each resistance group.

| Part | Configured HP | Resistance group | Physical damage × | Health rules |
| --- | --- | --- | --- | --- |
| DummyParent_Root | 1000 | Normal | 1 | 1 |
| Frame_01 | 20 | Critical | 1.5 | 0 |
| FrameCenterAxis | — | Normal | 1 |  |
| Hull_01 | 20 | Normal | 1 | 4 |
| PerceptionPart | — | Normal | 1 |  |

### Exact health assignment rules

| Rule | Tag query | HP | Matched parts |
| --- | --- | --- | --- |
| 0 | ID.Frame | 20 | Frame_01 |
| 1 | ID.Rollbot.Root | 1000 | DummyParent_Root |
| 2 | ID.Flap | 10 |  |
| 3 | ANY(ID.Arm) | 20 |  |
| 4 | ID.Head | 20 | Hull_01 |

### Self-destruct

The shared explosion effect sets **60 explosive damage** before falloff within a **3 m** targeting radius. [Effect](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Shared/Capabilities/GE_SharedPopSelfDestruct_Damage.json) · [Targeting](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Shared/Capabilities/GETT_SharedPopSelfDestruct.json) · [Radial curve](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Shared/Capabilities/Curve_SharedPop_Damage.json)

<details>
<summary>Destruction and stun rules</summary>

**Destruction groups**

| Part query | Destruction damage | Max level | Game file |
| --- | --- | --- | --- |
| ID.Frame | 1000 | 0.5 | [Actor config](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/C_RollBot_Pop.json) |
| ID.Weapon | 3000 | 1 | [Actor config](../Sources/PioneerGame/Content/Pioneer/Enemies/Pop/Pop/C_RollBot_Pop.json) |

</details>
