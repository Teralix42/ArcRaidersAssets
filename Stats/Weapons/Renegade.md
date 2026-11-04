# Renegade

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `BattleRifle_LeverAction_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Item_BattleRifle_LeverAction_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/DA_Item_BattleRifle_LeverAction_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_WeaponQualitySet_BattleRifle_LeverAction_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/BP_Projectile_BattleRifle_LeverAction_01.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 35 |
| Headshot multiplier | 2.25× |
| ARC armor multiplier | 0.8× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 45 |
| Magazine | 8 |
| Reload stat (s) | 3.5 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.003719 |
| Rounds loaded per reload loop | 1 |
| Reload loop entry (s) | 0.8 |
| Reload loop step (s) | 0.5 |
| Reload loop exit (s) | 0.4 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Fire rate (RPM) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- |
| II | +15 | −0.000372 | −16.666667% dispersion recovery speed |
| III | +30 | −0.000744 | −33.333333% dispersion recovery speed |
| IV | +45 | −0.001116 | −50% dispersion recovery speed |

### Amplified

Amplified default uses Level IV. Changes include Durability burn rate **−0.001301**.

[Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/BP_Item_BattleRifle_LeverAction_01_Ascended.json)

Changes are relative to the Amplified default. Where an upgrade has a prerequisite, its row includes the prerequisite’s changes.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| More Reload | Rounds loaded per reload loop **+1** | Increases the number of bullets loaded at a time, reducing reload time. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_MoreReload.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_MoreReload.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_MoreReload.json) |
| Scoped | Zoom modifier fraction **0.5** (game setting), Base zoom time **+0.2 s**, UI range score **+6.057**, UI stability score **−2.935** | Adds a scope to the weapon, allowing it to be fired from a scoped view. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_LeverAction_01_Scoped.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_LeverAction_01_Scoped.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/BP_Item_BattleRifle_LeverAction_01_Scoped.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_Item_BattleRifle_LeverAction_01_Scoped.json) · [Animation config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Ascended/Permutations/DA_ItemAnimationContainer_BattleRifle_LeverAction_01_Scoped.json) |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 35 |
| Armor | 11.2 |
| Sturdy | 14 |
| WeakPoint | 52.5 |
| Critical | 52.5 |
| Fragile | 42 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_LeverAction_01/Curve_DamageFalloff_BattleRifle_LeverAction_01.json)
