# Anvil

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Heavy · **Game ID:** `HandCannon_SingleAction_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Item_HandCannon_SingleAction_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/DA_Item_HandCannon_SingleAction_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_WeaponQualitySet_HandCannon_SingleAction_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/BP_Projectile_HandCannon_SingleAction_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 40 |
| Headshot multiplier | 2.5× |
| ARC armor multiplier | 1.5× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 40 |
| RPM interval (s) | 1.5 |
| Magazine | 6 |
| Input-buffer window (s) | 0.01 |
| Reload stat (s) | 2.5 |
| Firing mode | Semi-auto |
| Projectiles per shot | 1 |
| Damage if all projectiles hit | 40 |
| ARC armor propagation multiplier | 1× |
| Durability burn rate | 0.005333 |
| Rounds loaded per reload loop | 1 |
| Reload loop entry (s) | 0.8 |
| Reload loop step (s) | 0.7 |
| Reload loop exit (s) | 0.55 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Configured fire rate (RPM) | Durability burn rate | Handling modifiers | RPM interval (s) |
| --- | --- | --- | --- | --- |
| II | +10 | −0.000533 | −0.25 dispersion recovery speed | −0.3 |
| III | +20 | −0.001067 | −0.5 dispersion recovery speed | −0.5 |
| IV | +30 | −0.0016 | −0.75 dispersion recovery speed | −0.6429 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.001866** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/BP_Item_HandCannon_SingleAction_01_Ascended.json) |
| Anvil Splitter | Body damage / projectile **−28**, Headshot multiplier **−1×**, Projectiles per shot **+3**, Damage if all projectiles hit **+8**, −30% base dispersion, −90% dispersion recovery speed, +0.4 ADS dispersion scale, −100% max movement dispersion | Replaces the Anvil's bullets with rounds that split into four weaker projectiles. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_ProjectileSplitter.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_ProjectileSplitter.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_ProjectileSplitter.json) |
| X-Rounds | Body damage / projectile **+5**, Headshot multiplier **−0.25×**, ARC armor multiplier **+0.5×**, Damage if all projectiles hit **+5**, +30% vertical recoil, +30% horizontal recoil, −50% projectile speed | Adds an explosive compound to the projectile, dealing slightly increased damage to Raiders and significantly increased damage to ARC Armor plating. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/DA_Upgrade_HandCannon_SingleAction_01_XRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_HandCannon_SingleAction_01_XRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Ascended/Permutations/BP_Item_HandCannon_SingleAction_01_XRounds.json) |

**Mutually exclusive:** X-Rounds, Anvil Splitter.

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 40 |
| Armor | 24 |
| Sturdy | 16 |
| WeakPoint | 60 |
| Critical | 60 |
| Fragile | 48 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 180 | 1.001× | Linear |
| 200 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_SingleAction_01/Curve_DamageFalloff_HandCannon_SingleAction_01.json)
