# Hullcracker

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Launcher · **Game ID:** `Launcher_AntiArc_Medium_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/BP_Item_Launcher_AntiArc_Medium_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/DA_Item_Launcher_AntiArc_Medium_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/BP_WeaponQualitySet_Launcher_AntiArc_Medium_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/BP_Projectile_Launcher_AntiArc_Medium_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Impact damage against Raiders | 20 |
| ARC armor multiplier | 2.5× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 34 |
| RPM interval (s) | 1.7647 |
| Magazine | 5 |
| Input-buffer window (s) | 0.01 |
| Reload stat (s) | 3 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 0× |
| Durability burn rate | 0.004644 |
| Rounds loaded per reload loop | 1 |
| Reload loop entry (s) | 0.3 |
| Reload loop step (s) | 1.5 |
| Reload loop exit (s) | 0.3 |

### Firing, reload and impact details

- Explosive effect magnitude **100** within 1 m [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/BP_Projectile_Launcher_AntiArc_Medium_01.json) · [Targeting](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/GETT_Launcher_AntiARC_Medium_01.json) · [Radial curve](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Curve_RadialDamageFalloff_Launcher_AntiArc_Medium_01.json)

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Configured fire rate (RPM) | Durability burn rate | RPM interval (s) |
| --- | --- | --- | --- |
| II | +6 | −0.000464 | −0.2647 |
| III | +12 | −0.000929 | −0.4604 |
| IV | +18 | −0.001393 | −0.6109 |

### Amplified

Default changes are relative to Level IV; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.001626** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_Medium_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/BP_Item_Launcher_AntiArc_Medium_01_Ascended.json) |
| Incendiary Grenades | −50% projectile speed, Explosive effect magnitude **−40 (100 → 60)**, Burn **+1.125 thermal / 0.1 s tick**, **1.5 s** duration | Adds an incendiary compound to the projectile, causing it to spread fire when detonating on ARC. Explosive effect magnitude **60** within 1 m [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/BP_Projectile_Launcher_AntiArc_Medium_01_Incendiary.json) · [Targeting](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/GETT_Launcher_AntiARC_Medium_01.json) · [Radial curve](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Curve_RadialDamageFalloff_Launcher_AntiArc_Medium_01.json). 4 s lifetime, 1.125 thermal per 0.1 s tick, 1.5 s effect duration, 1 stack limit [Impact effect](../Sources/PioneerGame/Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json) · [Status effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json). | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_Medium_01_IncendiaryRounds.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_Medium_01_IncendiaryRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_Medium_01_IncendiaryRounds.json) |
| Mag Reload | Reload stat (s) **+2**, Partial-reload base duration (s) **5**, Refills the magazine in one action | Removes the need to reload one projectile at a time. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_Medium_01_MagReload.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_Medium_01_MagReload.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_Medium_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_Medium_01_MagReload.json) |
