[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Bantam

Internal weapon id: `HandCannon_DoubleAction_Snubnose_01`. Ammo: **HeavyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 24 | 1 | 24 | 1.5 | 1.5 | 1 | 300 | 8 | 3.4 |
| II | 24 | 1 | 24 | 1.5 | 1.5 | 1 | 300 | 8 | 2.9 |
| III | 24 | 1 | 24 | 1.5 | 1.5 | 1 | 300 | 8 | 2.4 |
| IV | 24 | 1 | 24 | 1.5 | 1.5 | 1 | 300 | 8 | 1.9 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | HandCannon_DoubleAction_Snubnose_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 24 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 24 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 300 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.4 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001 |
| Base partial-reload duration, seconds | 1.9 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 24 | 24 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9.6 | 9.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 28.8 | 28.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 24 |
| Fire rate | 23.333 |
| Range | 32.398 |
| Stability | 55.096 |
| Agility | 72.857 |
| Stealth | 9 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | 0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | HandCannon_DoubleAction_Snubnose_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 24 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 24 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 300 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.9 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0009 |
| Base partial-reload duration, seconds | 1.9 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 24 | 24 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9.6 | 9.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 28.8 | 28.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 24 |
| Fire rate | 23.333 |
| Range | 32.398 |
| Stability | 55.596 |
| Agility | 73.357 |
| Stealth | 9 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

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
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | HandCannon_DoubleAction_Snubnose_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 24 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 24 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 300 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.4 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0008 |
| Base partial-reload duration, seconds | 1.9 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 24 | 24 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9.6 | 9.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 28.8 | 28.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 24 |
| Fire rate | 23.333 |
| Range | 32.898 |
| Stability | 56.096 |
| Agility | 73.857 |
| Stealth | 9 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | HandCannon_DoubleAction_Snubnose_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 24 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 24 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 300 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.9 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0007 |
| Base partial-reload duration, seconds | 1.9 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 24 | 24 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 14.4 | 14.4 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9.6 | 9.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 36 | 36 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 28.8 | 28.8 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 24 |
| Fire rate | 23.333 |
| Range | 35.398 |
| Stability | 57.096 |
| Agility | 73.857 |
| Stealth | 9 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Dispersionrecoveryspeed

| Field | Value |
| --- | --- |
| Add | -0.4 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Item | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json |
| Quality set | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json)
- [Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json)

</details>
