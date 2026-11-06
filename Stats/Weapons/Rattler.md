# Rattler

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `AssaultRifle_LowTier_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Item_AssaultRifle_LowTier_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/DA_Item_AssaultRifle_LowTier_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_WeaponQualitySet_AssaultRifle_LowTier_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/BP_Projectile_AssaultRifle_LowTier_01.json) · [BP_Item_AssaultRifle_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 9 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 1× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 500 |
| RPM interval (s) | 0.12 |
| Magazine | 12 |
| Reload stat (s) | 3 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.001945 |
| Rounds loaded per reload loop | 2 |
| Reload loop entry (s) | 0.8 |
| Reload loop step (s) | 0.5 |
| Reload loop exit (s) | 0.2 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Magazine | Durability burn rate |
| --- | --- | --- |
| II | +4 | −0.000195 |
| III | +8 | −0.000389 |
| IV | +12 | −0.000584 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.00068** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Item_AssaultRifle_LowTier_01_Ascended.json) |
| Incendiary Rounds | Burn **+0.5 thermal / 0.1 s tick**, **2 s** duration, **1** stack maximum | Adds an incendiary compound to the projectile, setting targets on fire when hit. 0.5 thermal damage every 0.1 s for 2 s, up to 1 stack. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_IncendiaryRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_IncendiaryRounds.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/BP_Projectile_AssaultRifle_LowTier_Incendiary.json) · [Burning effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning_Small.json) |
| More Reload | Rounds loaded per reload loop **+2** | Increases the number of bullets loaded at a time, reducing reload time. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_MoreReload.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_MoreReload.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload.json) |
| Drum Mag (requires More Reload) | Magazine **+40**, Rounds loaded per reload loop **+2**, +50% vertical recoil, +50% horizontal recoil, +30% base dispersion, +50% max firing dispersion, +30% ADS dispersion scale, −10% ADS speed | Significantly increases magazine capacity by attaching a drum mag. However, it must still be reloaded a couple of bullets at time. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/DA_Upgrade_AssaultRifle_LowTier_01_DrumMag.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Upgrades/BP_UpgradeWeaponMod_AssaultRifle_LowTier_01_DrumMag.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Ascended/Permutations/BP_Item_AssaultRifle_LowTier_01_MoreReload_DrumMag.json) |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 9 |
| Armor | 3.6 |
| Sturdy | 3.6 |
| WeakPoint | 13.5 |
| Critical | 13.5 |
| Fragile | 10.8 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_LowTier_01/Curve_DamageFalloff_AssaultRifle_LowTier_01.json)
