# Osprey

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `SniperRifle_BoltAction_Medium_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Item_SniperRifle_BoltAction_Medium_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/DA_Item_SniperRifle_BoltAction_Medium_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_WeaponQualitySet_SniperRifle_BoltAction_Medium_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/BP_Projectile_SniperRifle_BoltAction_Medium_01.json) · [BP_Item_SniperRifle_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/SniperRifle_Base/BP_Item_SniperRifle_Base.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 45 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 0.8× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 45 |
| Magazine | 8 |
| Reload stat (s) | 4 |
| Cooldown (s) | 1.5 |
| Firing mode | Bolt-action |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.008775 |
| Partial-reload base duration (s) | 2.8 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Cooldown (s) | Durability burn rate |
| --- | --- | --- | --- |
| II | −0.5 | −0.1 | −0.002025 |
| III | −1 | −0.2 | −0.00405 |
| IV | −1.5 | −0.3 | −0.006075 |

### Amplified

Amplified default uses Level IV. Changes include Durability burn rate **−0.00135**.

[Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/BP_Item_SniperRifle_BoltAction_Medium_01_Ascended.json)

Changes are relative to the Amplified default. Where an upgrade has a prerequisite, its row includes the prerequisite’s changes.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Anti-Weak Point | ARC weak-point multiplier **+1×** | Deals increased damage to ARC weak points, but deals less damage to ARC armor plating. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_AntiWeakPoint.json) |
| Ergonomic Bolt | UI fire rate score **+2.143** | Ergonomic bolt that allows the user to perform the bolt-action while scoped. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_StraightBolt.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_StraightBolt.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_Item_SniperRifle_BoltAction_Medium_01_StraightBolt.json) · [Animation config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/DA_ItemAnimationContainer_SniperRifle_BoltAction_Medium_01_StraightBolt.json) |
| Tracker Rounds | −60% projectile speed, +5 tracking duration (s) | Replaces the bullets with tracker rounds that briefly reveal the position of targets they hit. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/DA_Upgrade_SniperRifle_BoltAction_Medium_01_TrackerRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_SniperRifle_BoltAction_Medium_01_TrackerRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Ascended/Permutations/BP_Item_SniperRifle_BoltAction_Medium_01_TrackerRounds.json) |

**Mutually exclusive:** Tracker Rounds, Anti-Weak Point.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 45 |
| Armor | 14.4 |
| Sturdy | 18 |
| WeakPoint | 67.5 |
| Critical | 67.5 |
| Fragile | 54 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SniperRifle_BoltAction_Medium_01/Curve_DamageFalloff_SniperRifle_BoltAction_Medium_01.json)
