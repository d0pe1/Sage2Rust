pub fn init() {
    println!("sage_core initialized");
}

pub mod ecs {
    use std::any::{Any, TypeId};
    use std::collections::HashMap;
    /// Unique identifier for spawned entities
    pub type EntityId = u32;

    /// Basic world state tracking the next entity id
    pub struct World {
        next_id: EntityId,
        storage: HashMap<EntityId, HashMap<TypeId, Box<dyn Any>>>,
    }

    impl World {
        pub fn new() -> Self {
            Self { next_id: 0, storage: HashMap::new() }
        }

        /// Reserve a new entity id without attaching any data yet
        pub fn spawn(&mut self) -> EntityId {
            let id = self.next_id;
            self.next_id += 1;
            self.storage.insert(id, HashMap::new());
            id
        }

        /// Convenience wrapper used by the engine to create a basic entity
        pub fn spawn_unit(&mut self) -> EntityId {
            self.spawn()
        }

        /// Attach a component instance to an entity
        pub fn add_component<C: Component>(&mut self, id: EntityId, component: C) {
            if let Some(entry) = self.storage.get_mut(&id) {
                entry.insert(TypeId::of::<C>(), Box::new(component));
            }
        }

        /// Retrieve a reference to a component of an entity
        pub fn get_component<C: Component>(&self, id: EntityId) -> Option<&C> {
            self.storage
                .get(&id)
                .and_then(|m| m.get(&TypeId::of::<C>()))
                .and_then(|b| b.downcast_ref())
        }
    }

    /// Marker trait for components stored in the world
    pub trait Component: 'static {}
}

#[cfg(test)]
mod tests {
    use super::ecs::*;

    #[test]
    fn spawn_entities_increment_id() {
        let mut world = World::new();
        assert_eq!(world.spawn_unit(), 0);
        assert_eq!(world.spawn_unit(), 1);
    }
}
