[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Rascal

Internal weapon id: `Launcher_AntiArc_SingleShot_01`. Ammo: **LauncherAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3.75 |
| II | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3.5 |
| III | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3.25 |
| IV | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3.75 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.007389 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

None.

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 4.67 |
| Range | 28.33 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00665 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

None.

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 7.67 |
| Range | 28.33 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3.25 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005911 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

None.

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 10.67 |
| Range | 28.33 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.25 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005172 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

None.

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 13.67 |
| Range | 28.33 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| High Velocity | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| High Velocity + Incendiary Grenades | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| High Velocity + Sprint Shooting | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| High Velocity + Sprint Shooting + Incendiary Grenades | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| Incendiary Grenades | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| Sprint Shooting | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |
| Sprint Shooting + Incendiary Grenades | 0 | 1 | 0 | — | 2.5 | 1 | 40 | 1 | 3 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

None.

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 13.67 |
| Range | 28.33 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Item_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/DA_Item_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — High Velocity

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity |
| Level | 5 |
| Level label | Amplified |
| Variant | High Velocity |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### High Velocity

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity |
| Name | High Velocity |
| Description | Increases the velocity of the projectile fired. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 13.67 |
| Range | 45 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — High Velocity + Incendiary Grenades

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | High Velocity + Incendiary Grenades |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### High Velocity

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity |
| Name | High Velocity |
| Description | Increases the velocity of the projectile fired. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Incendiary Grenades

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_IncendiaryRounds |
| Name | Incendiary Grenades |
| Description | Adds an incendiary compound to the projectile, causing it to spread fire when detonating on ARC. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 45 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 90 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 72 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 108 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 77.76 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

###### Item 1

| Field | Value |
| --- | --- |
| Type | impact_world_item |
| Source path | Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json |
| Lifetime s | 4 |
| Effect application interval s | 0.5 |
| Max particles | 6 |

**Gameplay effect**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json |
| Period s | 0.1 |
| Duration s | 1.5 |
| Execute on application | No |
| Stack limit | 1 |
| Stacking type | AggregateByTarget |

**Damage per period**

**Item 1**

| Field | Value |
| --- | --- |
| Damage type | Thermal |
| Amount | 1.125 |
| Resistance channel | fire |

**Arc direct damage per period by group**

**Normal**

| Field | Value |
| --- | --- |
| Resistance | 0 |
| Damage multiplier | 1 |
| Direct damage | 1.125 |

**Armor**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Sturdy**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Weakpoint**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Critical**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Fragile**

| Field | Value |
| --- | --- |
| Resistance | -0.2 |
| Damage multiplier | 1.2 |
| Direct damage | 1.35 |

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 45 |
| Fire rate | 13.67 |
| Range | 40 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.85 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — High Velocity + Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | High Velocity + Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### High Velocity

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity |
| Name | High Velocity |
| Description | Increases the velocity of the projectile fired. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 13.67 |
| Range | 45 |
| Stability | 87.8 |
| Agility | 83.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — High Velocity + Sprint Shooting + Incendiary Grenades

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | High Velocity + Sprint Shooting + Incendiary Grenades |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### High Velocity

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_HighVelocity |
| Name | High Velocity |
| Description | Increases the velocity of the projectile fired. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Zoomdispersionscale**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2 |
| Multiply | 1 |

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

###### Incendiary Grenades

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_IncendiaryRounds |
| Name | Incendiary Grenades |
| Description | Adds an incendiary compound to the projectile, causing it to spread fire when detonating on ARC. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 45 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 90 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 72 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 108 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 77.76 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

###### Item 1

| Field | Value |
| --- | --- |
| Type | impact_world_item |
| Source path | Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json |
| Lifetime s | 4 |
| Effect application interval s | 0.5 |
| Max particles | 6 |

**Gameplay effect**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json |
| Period s | 0.1 |
| Duration s | 1.5 |
| Execute on application | No |
| Stack limit | 1 |
| Stacking type | AggregateByTarget |

**Damage per period**

**Item 1**

| Field | Value |
| --- | --- |
| Damage type | Thermal |
| Amount | 1.125 |
| Resistance channel | fire |

**Arc direct damage per period by group**

**Normal**

| Field | Value |
| --- | --- |
| Resistance | 0 |
| Damage multiplier | 1 |
| Direct damage | 1.125 |

**Armor**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Sturdy**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Weakpoint**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Critical**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Fragile**

| Field | Value |
| --- | --- |
| Resistance | -0.2 |
| Damage multiplier | 1.2 |
| Direct damage | 1.35 |

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 45 |
| Fire rate | 13.67 |
| Range | 40 |
| Stability | 87.8 |
| Agility | 83.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Zoomdispersionscale

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.5 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.85 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Grenades

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Grenades |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### Incendiary Grenades

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_IncendiaryRounds |
| Name | Incendiary Grenades |
| Description | Adds an incendiary compound to the projectile, causing it to spread fire when detonating on ARC. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 45 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 90 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 72 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 108 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 77.76 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

###### Item 1

| Field | Value |
| --- | --- |
| Type | impact_world_item |
| Source path | Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json |
| Lifetime s | 4 |
| Effect application interval s | 0.5 |
| Max particles | 6 |

**Gameplay effect**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json |
| Period s | 0.1 |
| Duration s | 1.5 |
| Execute on application | No |
| Stack limit | 1 |
| Stacking type | AggregateByTarget |

**Damage per period**

**Item 1**

| Field | Value |
| --- | --- |
| Damage type | Thermal |
| Amount | 1.125 |
| Resistance channel | fire |

**Arc direct damage per period by group**

**Normal**

| Field | Value |
| --- | --- |
| Resistance | 0 |
| Damage multiplier | 1 |
| Direct damage | 1.125 |

**Armor**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Sturdy**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Weakpoint**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Critical**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Fragile**

| Field | Value |
| --- | --- |
| Resistance | -0.2 |
| Damage multiplier | 1.2 |
| Direct damage | 1.35 |

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 45 |
| Fire rate | 13.67 |
| Range | 23.33 |
| Stability | 87.8 |
| Agility | 78.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 75 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 150 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 120 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 60 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 91.2 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 225 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 144 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 180 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 129.6 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 75 |
| Fire rate | 13.67 |
| Range | 28.33 |
| Stability | 87.8 |
| Agility | 83.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Sprint Shooting + Incendiary Grenades

| Identity | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Sprint Shooting + Incendiary Grenades |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 0 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 0 |
| Firearm critical/headshot multiplier | — |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 0 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 40 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002586 |
| Base partial-reload duration, seconds | 3.15 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 0 | 0 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 0 | 0 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 0 | 0 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 0 | 0 |

##### Upgrades

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

###### Incendiary Grenades

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_IncendiaryRounds |
| Name | Incendiary Grenades |
| Description | Adds an incendiary compound to the projectile, causing it to spread fire when detonating on ARC. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json |
| Modifier function source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Launchspeed**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Extra damage effects

###### Item 1

| Field | Value |
| --- | --- |
| Damage type | Explosive |
| Effect magnitude | 45 |
| Target type | GETT_Launcher_AntiARC_SingleShot_01 |
| Ignore hit damage multipliers | No |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |
| Target source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json |
| Falloff source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Resistance channel | explosive |
| Damage values scope | One fully affected part before radial falloff, occlusion/exposure, global modifiers and health propagation; not guaranteed total damage of an explosion. |

**Arc direct damage by group**

**Normal**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1 |
| Damage multiplier | 2 |
| Direct damage | 90 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.6 |
| Damage multiplier | 1.6 |
| Direct damage | 72 |

**Armor**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Sturdy**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | 0.2 |
| Damage multiplier | 0.8 |
| Direct damage | 36 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.216 |
| Damage multiplier | 1.216 |
| Direct damage | 54.72 |

**Weakpoint**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Critical**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -2 |
| Damage multiplier | 3 |
| Direct damage | 135 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.92 |
| Damage multiplier | 1.92 |
| Direct damage | 86.4 |

**Fragile**

**Damage squish disabled**

| Field | Value |
| --- | --- |
| Resistance | -1.4 |
| Damage multiplier | 2.4 |
| Direct damage | 108 |

**Damage squish enabled**

| Field | Value |
| --- | --- |
| Resistance | -0.728 |
| Damage multiplier | 1.728 |
| Direct damage | 77.76 |

**Target settings**

| Field | Value |
| --- | --- |
| Radius | 100 |
| Baffectedbyocclusion | Yes |
| Busesphericocclusionsource | No |
| Spheresourceradius | 100 |
| Btargetconstructablesasactors | No |
| Baffectedbyfacingdirection | No |
| Constructabletargetinglevel | 1 |
| Bcheckteam | No |
| Btargetfriendly | Yes |
| Btargethostile | Yes |
| Btargetneutral | Yes |

**Objecttypes**

1, 0, 7, 6, 2, 8, 3, 9

**Damagefalloffcurve**

| Field | Value |
| --- | --- |
| Name | Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01 |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |

**Inline settings**

**Floatcurve**

**Keys**

| Interp mode | Tangent mode | Tangent weight mode | Time | Value | Arrive tangent | Arrive tangent weight | Leave tangent | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | 0.3 | 1 | -3.404799 | 0 | 0 | 0 |
| RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | 1 | 0.25 | -0.028422 | 0 | -0.028422 | 0 |

**Target geometry**

| Field | Value |
| --- | --- |
| Configured radius cm | 100 |
| Configured radius m | 1 |
| Spherical source radius cm | 100 |
| Affected by occlusion | Yes |
| Affected by facing direction | No |
| Target constructables as actors | No |
| Constructable targeting level index | 1 |

**Object type query indices**

1, 0, 7, 6, 2, 8, 3, 9

**Radial falloff**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json |
| Input units | distance divided by configured radius, clamped to 0..1 |
| Output units | affected-degree factor, clamped to 0..1 |

**Keys**

| Distance fraction of radius | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.3 | 1 | RCIM_Cubic | RCTM_Auto | RCTWM_WeightedNone | -3.404799 | 0 | 0 | 0 |
| 1 | 0.25 | RCIM_Cubic | RCTM_User | RCTWM_WeightedNone | -0.028422 | -0.028422 | 0 | 0 |

**Stored settings not serialized**

pre_infinity_extrapolation, post_infinity_extrapolation

##### Secondary effects

###### Item 1

| Field | Value |
| --- | --- |
| Type | impact_world_item |
| Source path | Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json |
| Lifetime s | 4 |
| Effect application interval s | 0.5 |
| Max particles | 6 |

**Gameplay effect**

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json |
| Period s | 0.1 |
| Duration s | 1.5 |
| Execute on application | No |
| Stack limit | 1 |
| Stacking type | AggregateByTarget |

**Damage per period**

**Item 1**

| Field | Value |
| --- | --- |
| Damage type | Thermal |
| Amount | 1.125 |
| Resistance channel | fire |

**Arc direct damage per period by group**

**Normal**

| Field | Value |
| --- | --- |
| Resistance | 0 |
| Damage multiplier | 1 |
| Direct damage | 1.125 |

**Armor**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Sturdy**

| Field | Value |
| --- | --- |
| Resistance | 0.6 |
| Damage multiplier | 0.4 |
| Direct damage | 0.45 |

**Weakpoint**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Critical**

| Field | Value |
| --- | --- |
| Resistance | -0.5 |
| Damage multiplier | 1.5 |
| Direct damage | 1.6875 |

**Fragile**

| Field | Value |
| --- | --- |
| Resistance | -0.2 |
| Damage multiplier | 1.2 |
| Direct damage | 1.35 |

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Non arc impact damage | 20 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 45 |
| Fire rate | 13.67 |
| Range | 23.33 |
| Stability | 87.8 |
| Agility | 83.1 |
| Stealth | 1 |

##### Damage falloff

—

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

###### Launchspeed

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json |
| Quality function package | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.uasset |
| Projectile | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Launcher_AntiArc_SingleShot_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Item_Launcher_AntiArc_SingleShot_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Item_Launcher_AntiArc_SingleShot_01_Ascended.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/BP_Projectile_Launcher_AntiArc_SingleShot_01_Incendiary.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/DA_Item_Launcher_AntiArc_SingleShot_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/DA_Item_Launcher_AntiArc_SingleShot_01_Ascended.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/BP_Item_Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_HighVelocity_SprintShooting_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_SprintShooting.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Permutations/DA_Item_Launcher_AntiArc_SingleShot_01_SprintShooting_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_HighVelocity.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Launcher_AntiArc_SingleShot_01_SprintShooting.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_Ascended.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_HighVelocity.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Ascended/Upgrades/DA_Upgrade_Launcher_AntiArc_SingleShot_01_SprintShooting.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Item_Launcher_AntiArc_SingleShot_01.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_Projectile_Launcher_AntiArc_SingleShot_01.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/BP_WeaponQualitySet_Launcher_AntiArc_SingleShot_01.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/Curve_RadialDamageFalloff_Launcher_AntiArc_SingleShot_01.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/DA_Item_Launcher_AntiArc_SingleShot_01.json)
- [Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Launchers/Launcher_AntiArc_SingleShot_01/GETT_Launcher_AntiARC_SingleShot_01.json)
- [Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Shared/Damage/BP_WItem_IncendiarySpread_Ascended.json)

</details>
