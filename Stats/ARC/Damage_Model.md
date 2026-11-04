# ARC damage and resistance

[ARC stats](README.md) · [Weapons](../Weapons/)

| Part group | Physical resistance | Physical, fire, electric and melee × | Explosive ×, flag off | Explosive ×, flag on |
| --- | --- | --- | --- | --- |
| Normal | 0% | 1 | 2 | 1.6 |
| Armor | 60% | 0.4 | 0.8 | 1.216 |
| Sturdy | 60% | 0.4 | 0.8 | 1.216 |
| WeakPoint | −50% | 1.5 | 3 | 1.92 |
| Critical | −50% | 1.5 | 3 | 1.92 |
| Fragile | −20% | 1.2 | 2.4 | 1.728 |

These factors apply to damage directly received by a part. Frame HP, damage propagation, and destruction rules are separate and depend on the machine.

- **Physical** starts with `1 − resistance`. For Armor, multiply by the weapon’s ARC armor multiplier and cap at 1×. For WeakPoint and Critical, multiply by the weapon’s ARC weak-point multiplier.
- **Fire, electric and melee** use their own resistance channels. Their configured factors match the base physical factors in this build.
- **Explosive** uses `2 × (1 − physical resistance)` with `constructable_explosive_damage_squish` disabled and `1.6 × (1 − 0.4 × physical resistance)` with it enabled. The active session setting is unknown. Blast exposure can include the radial falloff curve.

Part tags and health rules link directly to the game exports on each ARC page. Resistance values and damage formulas were recovered from `PioneerGame/Script/PrecompiledScript.Cache` in Steam changelist `1438640`. The relevant symbols are `ConstructableResistances::GetResistancesForGroup`, `CalcExplosiveResistance`, and `UPioneerDamageCalculation::ConsumeDamageWithPerPartResistance`.
