# Jupiter

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Energy · **Game ID:** `Special_Railgun_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Item_Special_Railgun_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/DA_Item_Special_Railgun_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_WeaponQualitySet_Special_Railgun_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/BP_Projectile_Special_Railgun_01.json)

### Standard

| Stat | Value |
| --- | --- |
| Body damage / projectile | 60 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 3× |
| ARC weak-point multiplier | 1.3× |
| Fire rate (RPM) | 45 |
| Magazine | 5 |
| Reload stat (s) | 3 |
| Cooldown (s) | 2 |
| Firing mode | Bolt-action |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.0045 |
| Partial-reload base duration (s) | 3.3 |

### Firing, reload and impact details

- Initial charge delay (s) **0.75**
- Damage multiplier per penetrated hit **0.75**
- Extra hipfire windup (s) **0.2**
- Skip extra hipfire windup in combat
- Standard and Amplified share the reload animation and timing config. [Shared reload animation](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/DA_WeaponAnimations_Special_Railgun_01.json)

### Amplified

Amplified default uses the standard weapon as its baseline. Changes include Durability burn rate **−0.00225**.

[Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/BP_Item_Special_Railgun_01_Ascended.json)

Changes are relative to the Amplified default. Where an upgrade has a prerequisite, its row includes the prerequisite’s changes.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Bigger Mag | Magazine **+5** | Increases the magazine capacity. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_BiggerMag.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_BiggerMag.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_BiggerMag.json) |
| Scoped | Zoom modifier fraction **0.5** (game setting), UI range score **+4.904** | Adds a scope to the weapon, allowing it to be fired from a scoped view. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_Scoped.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_Scoped.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_Scoped.json) · [Animation config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_ItemAnimationContainer_Special_Railgun_01_Scoped.json) |
| Ergonomic Bolt | UI fire rate score **+3** | Ergonomic bolt that allows the user to perform the bolt-action while scoped. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/DA_Upgrade_Special_Railgun_01_StraightBolt.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Special_Railgun_01_StraightBolt.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/BP_Item_Special_Railgun_01_StraightBolt.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_Item_Special_Railgun_01_StraightBolt.json) · [Animation config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Ascended/Permutations/DA_ItemAnimationContainer_Special_Railgun_01_StraightBolt.json) |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 60 |
| Armor | 60 |
| Sturdy | 24 |
| WeakPoint | 117 |
| Critical | 117 |
| Fragile | 72 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 180 | 1.001× | Linear |
| 200 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Special_Railgun_01/Curve_DamageFalloff_Special_Railgun_01.json)
