# Rascal

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Launcher · **Game ID:** `Launcher_AntiArc_SingleShot_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Impact damage against Raiders | 20 |
| ARC armor multiplier | 2.5× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 40 |
| RPM interval (s) | 1.5 |
| Magazine | 1 |
| Input-buffer window (s) | 0.01 |
| Automatic-reload start delay (s) | 0.4 |
| Reload stat (s) | 3.75 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 0× |
| Durability burn rate | 0.007389 |
| Partial-reload base duration (s) | 3.15 |

### Firing, reload and impact details

- Explosive effect magnitude **75** within 1 m [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json) · [Targeting](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json) · [Radial curve](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json)

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate |
| --- | --- | --- |
| II | −0.25 | −0.000739 |
| III | −0.5 | −0.001478 |
| IV | −0.75 | −0.002217 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.002586** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Item_Launcher_AntiArc_SingleShot_01_Ascended.json) |
| High Velocity | +100% projectile speed, −50% ADS dispersion scale | Increases the velocity of the projectile fired. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json) |
| Incendiary Grenades | −15% projectile speed, Explosive effect magnitude **−30 (75 → 45)**, Burn **+1.125 thermal / 0.1 s tick**, **1.5 s** duration | Adds an incendiary compound to the projectile, causing it to spread fire when detonating on ARC. Explosive effect magnitude **45** within 1 m [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json) · [Targeting](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json) · [Radial curve](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json). 4 s lifetime, 1.125 thermal per 0.1 s tick, 1.5 s effect duration, 1 stack limit [Impact effect](../Sources/PioneerGame/Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json) · [Status effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json). | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json) |
| Sprint Shooting | Firing while sprinting **enabled** | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json) |
