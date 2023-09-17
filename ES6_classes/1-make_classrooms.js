import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const roomSize = [19, 20, 34];
  const roomsList = [];
  for (const room of roomSize) {
    const addRoom = new ClassRoom(room);
    roomsList.push(addRoom);
  }
  return roomsList;
}

initializeRooms();
