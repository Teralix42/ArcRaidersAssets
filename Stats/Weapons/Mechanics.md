# Weapon mechanics and field definitions

Common definitions, resistance values, and native source evidence. Individual weapon pages contain their level and amplified-configuration tables.

**Coverage:** 26 weapon families; 92 standard-level records; 89 amplified configurations.

Source paths are relative to `PioneerGame` and are provenance only. `—` means unknown or not applicable, never zero. This is configured/derived data, not live combat measurement.

## Weapon index

- [Anvil](Anvil.md)
- [Aphelion](Aphelion.md)
- [Arpeggio](Arpeggio.md)
- [Bantam](Bantam.md)
- [Bettina](Bettina.md)
- [Bobcat](Bobcat.md)
- [Burletta](Burletta.md)
- [Canto](Canto.md)
- [Dolabra](Dolabra.md)
- [Equalizer](Equalizer.md)
- [Ferro](Ferro.md)
- [Hairpin](Hairpin.md)
- [Hullcracker](Hullcracker.md)
- [Il Toro](Il%20Toro.md)
- [Jupiter](Jupiter.md)
- [Kettle](Kettle.md)
- [Osprey](Osprey.md)
- [Rascal](Rascal.md)
- [Rattler](Rattler.md)
- [Renegade](Renegade.md)
- [Stiletto](Stiletto.md)
- [Stitcher](Stitcher.md)
- [Tempest](Tempest.md)
- [Torrente](Torrente.md)
- [Venator](Venator.md)
- [Vulcano](Vulcano.md)

## Field definitions

| Field | Meaning |
| --- | --- |
| level | Standard level I-IV is UpgradeLevel 1-4. Amplified UI UpgradeLevel is 5, using the item's BaseQualityLevel (normally standard IV). Weapons without levels retain level=null. |
| physical_damage_per_projectile | Physical damage for one projectile before falloff, hit location, shield/ARC resistance and damage propagation. Extra explosive/fire effects are separate. |
| physical_damage_full_spread | All simultaneous physical projectiles hitting. Bursts are separate. Null for special hit-normalisation weapons such as Dolabra. |
| critical_damage_multiplier | Firearm critical/headshot setting; separate from the ARC weakpoint setting and the part's resistance group. |
| fire_rate_rpm | Modified BaseFireRate; for burst weapons this is within-burst cadence, not sustained rate including cooldown/reload. |
| burst_size | Modified BurstSize stat; charge mechanics can change actual rounds fired. See conditional_mechanics for minimum burst size and charge time per extra shot. |
| reload_time_stat_s | Modified BaseReloadTime stat. Partial/shell animation timings are retained separately as base values, not claimed as measured complete reload duration. |
| ui_stat_scores | Inventory display scores, including range; not direct physical distance, RPM or measured accuracy. |
| extra_damage_effects | Effect magnitudes and target definitions; not guaranteed total damage per target. |
| modifiers | Auditable coefficients: Add, AddMultiply (identity=1), Multiply (identity=1). Add components combine by addition, AddMultiply by adding deltas from 1, and Multiply by multiplication. Final native arithmetic was not recovered for mixed Add/AddMultiply fields; these are null with candidates in unresolved_stats. |
| modifier_selection | Use BakedModifiersDelta only when bHasGeneratedBakedModifiers is true; otherwise use the decoded ModifyWeaponAttributes graph. Disabled cached deltas can be stale. |
| arc_direct_damage | Numeric direct physical damage for every resistance group, with this variant's ARC armour and weakpoint multipliers already applied. Reference conditions and limits are embedded in the same object/file. |
| damage_model | Complete numeric physical/fire/electric/melee resistance and damage factors plus both explosive feature-flag branches. No external resistance lookup is required. |
| source_paths | Optional provenance only; the exported numeric values, curves, target settings and upgrade modifiers are included directly. |

## Damage and resistance model

One part's direct damage stage, before downstream health propagation or destruction chains. Distance, radial exposure, global damage modifiers, and skill modifiers are separate inputs.

Resistance is a fraction: `0.6` means 60% resistance and a baseline `0.4×` damage factor. Negative resistance increases damage. These are direct part-damage stages; propagation into frame health is separate.

| Group | Physical R | Physical × | Fire R | Fire × | Electric × | Melee × | Explosive off: R / × | Explosive on: R / × |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 0 | 1 | 1 | 1 | -1 / 2× | -0.6 / 1.6× |
| Armor | 0.6 | 0.4 | 0.6 | 0.4 | 0.4 | 0.4 | 0.2 / 0.8× | -0.216 / 1.216× |
| Sturdy | 0.6 | 0.4 | 0.6 | 0.4 | 0.4 | 0.4 | 0.2 / 0.8× | -0.216 / 1.216× |
| WeakPoint | -0.5 | 1.5 | -0.5 | 1.5 | 1.5 | 1.5 | -2 / 3× | -0.92 / 1.92× |
| Critical | -0.5 | 1.5 | -0.5 | 1.5 | 1.5 | 1.5 | -2 / 3× | -0.92 / 1.92× |
| Fragile | -0.2 | 1.2 | -0.2 | 1.2 | 1.2 | 1.2 | -1.4 / 2.4× | -0.728 / 1.728× |

Thermal damage uses the fire-resistance channel. Electric and melee resistances equal the physical/fire resistance in this snapshot. All five channels and both explosive branches are included numerically in this document.

### Formulas

| Field | Value |
| --- | --- |
| Basic damage taken multiplier | 1 - resistance |
| Physical normal sturdy fragile | physical_damage_per_projectile * (1 - physical_resistance) |
| Physical armor | physical_damage_per_projectile * clamp((1 - physical_resistance) * weapon_arc_armor_damage_multiplier, 0, 1) |
| Physical weakpoint and critical | physical_damage_per_projectile * (1 - physical_resistance) * weapon_arc_weakpoint_damage_multiplier |
| Non physical damage | input_damage_of_that_type * (1 - resistance_of_that_type) |
| Explosive flag disabled | explosive_damage_multiplier = (1 - physical_resistance) * 2 |
| Explosive flag enabled | explosive_damage_multiplier = (1 - 0.4 * physical_resistance) * 1.6 |
| Distance and area | Multiply the direct stage by the weapon distance factor and the attack's affected-degree/exposure factor. A spherical target routine already includes radial falloff in its affected degree; do not apply that radial curve twice. |
| Sphere radial curve input | clamp(distance_cm / configured_radius_cm, 0, 1) |
| Sphere radial curve output | clamp(radial_curve(normalized_distance), 0, 1) |
| Sphere radial without curve | 1 - clamp(distance_cm / configured_radius_cm, 0, 1) |

### Reference conditions

| Field | Value |
| --- | --- |
| Distance falloff multiplier | 1 |
| Affected degree or exposure | 1 |
| Global damage multiplier | 1 |
| Other skill or session modifiers | 1 |

### Explosive runtime flag

| Field | Value |
| --- | --- |
| Name | constructable_explosive_damage_squish |
| Active state | — |
| Reason | The cache calls the runtime feature-flag service. Its active server/session value is not present in this offline dataset. Both numeric branches are included on every assigned part. |

### Unmapped resistance-type fallback

| Field | Value |
| --- | --- |
| Resistance | 0 |
| Damage taken multiplier | 1 |
| Meaning | GetResistanceForType returns this for a resistance-type enum outside the five supported channels. This does not assign a group to an unclassified mesh record. |

### Interpretation

- Resistance 0.6 means a baseline 0.4x damage factor; resistance -0.5 means 1.5x damage. Negative resistance is vulnerability.
- Armor and Sturdy share baseline resistance but only Armor receives the physical weapon ARC-armour multiplier.
- The firearm critical/headshot multiplier is not automatically applied to the ARC Critical resistance group. ARC weak/critical parts use the separate ARC weakpoint multiplier in this calculation.
- Weapon ARC-armour and weakpoint multipliers are applied by the recovered physical damage branch, not to explosive/thermal/electric effect magnitudes by this branch.
- Armor propagation multipliers describe another stage; the direct numbers here are not automatically frame-health damage or total damage-to-kill.
- A part without a serialized resistance-group assignment retains null numeric values. Several such records are sockets, muzzle bones, or visual/proxy components; their group is not guessed from their name or health tags.

### Model provenance

| Field | Value |
| --- | --- |
| Path | Script/PrecompiledScript.Cache |
| Sha256 | 120a31ba704fa8f9c634f8458d83f82fc2954fbe8b0a91d923a708584ebb59b8 |

#### Functions

ConstructableResistances::GetResistancesForGroup, FConstructablePartResistances.GetResistanceForType, ConstructableResistances::Internal::CalcExplosiveResistance, UPioneerDamageCalculation.ConsumeDamageWithPerPartResistance, UPioneerDamageCalculation.ExecuteDamageConstructables, TargetingUtils::CalculateAffectedDegreeUNormByDistance, CalculateDamage

[Back to weapon index](README.md)
