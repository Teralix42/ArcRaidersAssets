# Weapon mechanics

[Weapons](README.md) · [ARC damage model](../ARC/Damage_Model.md) · [Shields](../Shields/)

The tables use the Steam 2.4 game files. Values come from weapon blueprints, inherited defaults, level modifiers, and upgrade assets. Each page links to the corresponding property exports.

### Damage and firing

- Body damage uses a 1× hit before falloff and shields. Headshots use the listed multiplier. ARC armor and weak points use their own multipliers.
- Projectiles per shot counts simultaneous projectiles, such as pellets. Shots per burst counts consecutive shots. For bursts, RPM is the cadence within a burst. Cooldown and reload affect sustained fire.
- Damage falloff lists the curve’s configured control points. Impact effects such as explosions and burning have their own targeting, damage, and timing.

### Reloads and upgrades

- The reload stat comes from `BaseReloadTime` and its modifiers. Partial reloads have separate timing. For weapons that reload in a loop, the entry, loop step, exit, and rounds loaded per step are listed separately. Actual time depends on how the reload starts and how many steps run.
- Level II–IV deltas are relative to Level I. Amplified upgrades are relative to the Amplified default. Where an upgrade requires another node, its row includes the prerequisite’s changes.
- Handling modifiers describe changes to game settings. Inventory scores describe the tooltip bars. A scope’s zoom modifier fraction is a game setting.
- For weapons with cached modifier data, the game uses the baked delta when `bHasGeneratedBakedModifiers` is enabled. Otherwise the source is the package’s `ModifyWeaponAttributes` graph. The Semi-Auto RPM on Bettina and Hairpin has two possible readings because the native operation order for their mixed modifiers is unverified.

Inherited weapon defaults and modifier arithmetic come from `PioneerGame/Script/PrecompiledScript.Cache` in Steam changelist `1438640`. Relevant symbols include `UWeaponItem`, `FWeaponModifiers`, and `FWeaponStatModifier`.
