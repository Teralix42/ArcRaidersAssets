# Il Toro

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Shotgun · **Game ID:** `Shotgun_PumpAction_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Item_Shotgun_PumpAction_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/DA_Item_Shotgun_PumpAction_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_WeaponQualitySet_Shotgun_PumpAction_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/BP_Projectile_Shotgun_PumpAction_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 7 |
| Headshot multiplier | 1× |
| ARC armor multiplier | 0.5× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 38.25 |
| RPM interval (s) | 1.5686 |
| Magazine | 5 |
| Input-buffer window (s) | 0.01 |
| Reload stat (s) | 2.5 |
| Firing mode | Semi-auto |
| Projectiles per shot | 9 |
| Damage if all projectiles hit | 63 |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.007378 |
| Rounds loaded per reload loop | 1 |
| Reload loop entry (s) | 1 |
| Reload loop step (s) | 0.7 |
| Reload loop exit (s) | 0.5 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Configured fire rate (RPM) | Magazine | Durability burn rate | RPM interval (s) |
| --- | --- | --- | --- | --- |
| II | +6.75 | +1 | −0.000738 | −0.2353 |
| III | +13.5 | +2 | −0.001476 | −0.4092 |
| IV | +20.25 | +3 | −0.002213 | −0.543 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.002583** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/BP_Item_Shotgun_PumpAction_01_Ascended.json) |
| More Reload | Rounds loaded per reload loop **+1** | Increases the number of bullets loaded at a time, reducing reload time. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_MoreReload.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_MoreReload.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_MoreReload.json) |
| Slug Rounds | Body damage / projectile **+63**, ARC armor multiplier **+1×**, Projectiles per shot **−8**, Damage if all projectiles hit **+7**, ARC armor propagation multiplier **+0.6×**, −50% projectile speed, −40% base dispersion, −20% falloff distance scale | Replaces the normal shotgun shells with a single large projectile that deals massive damage. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/DA_Upgrade_Shotgun_PumpAction_01_SlugRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Shotgun_PumpAction_01_SlugRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Ascended/Permutations/BP_Item_Shotgun_PumpAction_01_SlugRounds.json) |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 7 |
| Armor | 1.4 |
| Sturdy | 2.8 |
| WeakPoint | 10.5 |
| Critical | 10.5 |
| Fragile | 8.4 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 20 | 1.001× | Linear |
| 50 | 0.5× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_PumpAction_01/Curve_DamageFalloff_Shotgun_PumpAction_01.json)
