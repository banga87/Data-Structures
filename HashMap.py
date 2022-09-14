class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(self.array_size)]

    def hash(self, key, num_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + num_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        current_array_index = self.compressor(hash(key))
        current_array_value = self.array[current_array_index]

        # No value
        if current_array_value is None:
            self.array[current_array_index] = [key, value]
            return

        # Same key
        if current_array_value[0] is key:
            self.array[current_array_index] = [key, value]

        # Collision

        collisions = 1

        while current_array_value[0] != key:
            new_array_index = self.compressor(hash(key, collisions))
            new_array_value = self.array[new_array_index]

            # No value
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            # Same key
            if current_array_value[0] is key:
                self.array[current_array_index] = [key, value]
                return

            # Collision
            collisions += 1
        
        return 
