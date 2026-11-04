[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Venator

Internal weapon id: `Pistol_HighPower_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 8 | 2 | 16 | 2 | 0.8 | 1 | 225 | 10 | 3.5 |
| II | 8 | 2 | 16 | 2 | 0.8 | 1 | 255 | 10 | 3 |
| III | 8 | 2 | 16 | 2 | 0.8 | 1 | 285 | 10 | 2.5 |
| IV | 8 | 2 | 16 | 2 | 0.8 | 1 | 315 | 10 | 2 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | Pistol_HighPower_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 2 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 225 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001378 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 16 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.56 | 5.12 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 19.2 |

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
| Damage | 16 |
| Fire rate | 23.67 |
| Range | 48.38 |
| Stability | 64.8 |
| Agility | 76.4 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | -30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | Pistol_HighPower_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 2 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 255 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00124 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 16 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.56 | 5.12 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 19.2 |

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
| Damage | 16 |
| Fire rate | 26.67 |
| Range | 48.38 |
| Stability | 61.3 |
| Agility | 76.4 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | Pistol_HighPower_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 2 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 285 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001102 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 16 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.56 | 5.12 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 19.2 |

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
| Damage | 16 |
| Fire rate | 29.67 |
| Range | 48.38 |
| Stability | 57.8 |
| Agility | 76.4 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | Pistol_HighPower_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 2 |
| Physical damage / full spread | 16 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 315 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 2 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000965 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 16 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 2.56 | 5.12 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 6.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 24 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 19.2 |

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
| Damage | 16 |
| Fire rate | 32.67 |
| Range | 48.38 |
| Stability | 54.8 |
| Agility | 76.4 |
| Stealth | 12 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 60 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json)

</details>
