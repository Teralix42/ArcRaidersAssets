[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Hairpin

Internal weapon id: `Pistol_Silenced_01`. Ammo: **LightAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 55.5 | 8 | 3 |
| II | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 60 | 8 | 2.5 |
| III | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 64.5 | 8 | 2 |
| IV | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 69 | 8 | 1.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 55.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003673 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

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
| Damage | 20 |
| Fire rate | 8.5 |
| Range | 37.995 |
| Stability | 92.623 |
| Agility | 77.812 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Add | -4.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 60 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003306 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

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
| Damage | 20 |
| Fire rate | 9 |
| Range | 37.995 |
| Stability | 92.123 |
| Agility | 78.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 64.5 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 2 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002938 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

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
| Damage | 20 |
| Fire rate | 9.5 |
| Range | 37.995 |
| Stability | 91.623 |
| Agility | 78.812 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Add | 4.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 69 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.002571 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

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
| Damage | 20 |
| Fire rate | 10 |
| Range | 37.995 |
| Stability | 91.123 |
| Agility | 79.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Add | 9 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 69 | 8 | 1.5 |
| Incendiary Rounds | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 69 | 8 | 1.5 |
| Semi-Auto | 20 | 1 | 20 | 2 | 0.2 | 1 | — | 8 | 1.5 |
| Semi-Auto + Sprint Shooting | 20 | 1 | 20 | 2 | 0.2 | 1 | — | 8 | 1.5 |
| Tracker Rounds | 20 | 1 | 20 | 2.5 | 0.2 | 1 | 69 | 8 | 1.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 69 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001286 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

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
| Damage | 20 |
| Fire rate | 10 |
| Range | 37.995 |
| Stability | 91.123 |
| Agility | 79.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Add | 9 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Item_Pistol_Silenced_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/DA_Item_Pistol_Silenced_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 69 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001286 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

##### Upgrades

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

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
| Damage | 20 |
| Fire rate | 10 |
| Range | 37.995 |
| Stability | 91.123 |
| Agility | 79.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Add | 9 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Projectile_Pistol_Silenced_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Semi-Auto

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_SemiAuto |
| Level | 5 |
| Level label | Amplified |
| Variant | Semi-Auto |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | — |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001286 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

##### Upgrades

###### Semi-Auto

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_SemiAuto |
| Name | Semi-Auto |
| Description | Makes the weapon semi-automatic. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SemiAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2.5 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 10 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firedispersiongain**

| Field | Value |
| --- | --- |
| Add | 0.4 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 20 |
| Fire rate | 12.5 |
| Range | 37.995 |
| Stability | 72.943 |
| Agility | 79.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Unresolved stats

###### Firerate

| Field | Value |
| --- | --- |
| Reason | Add and AddMultiply are both active; native CalculateCurrent operation order was not recovered. |
| Base | 60 |

**Modifier**

| Field | Value |
| --- | --- |
| Add | 9 |
| Addmultiply | 2.5 |
| Multiply | 1 |

**Candidate values**

159, 172.5

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
| Add | 9 |
| Addmultiply | 2.5 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 10 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0.4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_SemiAuto.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Semi-Auto + Sprint Shooting

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_SemiAuto_SprintShooting |
| Level | 5 |
| Level label | Amplified |
| Variant | Semi-Auto + Sprint Shooting |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | — |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001286 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

##### Upgrades

###### Semi-Auto

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_SemiAuto |
| Name | Semi-Auto |
| Description | Makes the weapon semi-automatic. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SemiAuto.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Criticaldamagemultiplier**

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firerate**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 2.5 |
| Multiply | 1 |

**Firedispersionmax**

| Field | Value |
| --- | --- |
| Add | 10 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firedispersiongain**

| Field | Value |
| --- | --- |
| Add | 0.4 |
| Addmultiply | 1 |
| Multiply | 1 |

**Firingmodeoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

###### Sprint Shooting

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_SprintShooting |
| Name | Sprint Shooting |
| Description | Ergonomic fittings that allow the weapon to be comfortably fired while sprinting. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SprintShooting.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SprintShooting.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SprintShooting.uasset |
| Modifier selection | baked_cache_enabled |

**Modifiers**

**Blocksprintoverride**

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 20 |
| Fire rate | 12.5 |
| Range | 37.995 |
| Stability | 72.943 |
| Agility | 84.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Unresolved stats

###### Firerate

| Field | Value |
| --- | --- |
| Reason | Add and AddMultiply are both active; native CalculateCurrent operation order was not recovered. |
| Base | 60 |

**Modifier**

| Field | Value |
| --- | --- |
| Add | 9 |
| Addmultiply | 2.5 |
| Multiply | 1 |

**Candidate values**

159, 172.5

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
| Add | 9 |
| Addmultiply | 2.5 |
| Multiply | 1 |

###### Criticaldamagemultiplier

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 10 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firedispersiongain

| Field | Value |
| --- | --- |
| Add | 0.4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firingmodeoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Currentfiringmode | EFiringMode::SemiAuto |

###### Blocksprintoverride

| Field | Value |
| --- | --- |
| Boverridden | Yes |
| Bblocksprintduringprimaryuse | No |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Tracker Rounds

| Identity | Value |
| --- | --- |
| Id | Pistol_Silenced_01_TrackerRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Tracker Rounds |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 20 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 20 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 69 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 1.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001286 |
| Base partial-reload duration, seconds | 1.4 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 20 | 20 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 1.6 | 1.6 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 8 | 8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 30 | 30 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 24 | 24 |

##### Upgrades

###### Tracker Rounds

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_TrackerRounds |
| Name | Tracker Rounds |
| Description | Replaces the bullets with tracker rounds that briefly reveal the position of targets they hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_TrackerRounds.json |
| Modifier source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_TrackerRounds.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_TrackerRounds.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Taggingtime**

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 20 |
| Fire rate | 10 |
| Range | 37.995 |
| Stability | 91.123 |
| Agility | 79.312 |
| Stealth | 70 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Add | 9 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Taggingtime

| Field | Value |
| --- | --- |
| Add | 5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_TrackerRounds.json |
| Item | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_TrackerRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | Pistol_Silenced_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Item_Pistol_Silenced_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Item_Pistol_Silenced_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Projectile_Pistol_Silenced_Incendiary.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/BP_Projectile_Pistol_Silenced_Incendiary.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/DA_Item_Pistol_Silenced_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/DA_Item_Pistol_Silenced_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/BP_Item_Pistol_Silenced_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_SemiAuto_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Permutations/DA_Item_Pistol_Silenced_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/BP_UpgradeWeaponMod_Pistol_Silenced_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SemiAuto.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SemiAuto.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SprintShooting.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_SprintShooting.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_TrackerRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Ascended/Upgrades/DA_Upgrade_Pistol_Silenced_01_TrackerRounds.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Item_Pistol_Silenced_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_Projectile_Pistol_Silenced_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/BP_WeaponQualitySet_Pistol_Silenced_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/Curve_DamageFalloff_Pistol_Silenced_01.json)
- [Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_Silenced_01/DA_Item_Pistol_Silenced_01.json)
- [Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/Pistol_Base/BP_Item_Pistol_Base.json)

</details>
