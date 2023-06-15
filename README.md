# **_Showtime_**

## Date: 6/15/2023

### Authors: [Cody Garcia](https://github.com/popgoesthecultureshock), [Austin Showen](https://github.com/austin-showen), [Jacquelyn Waller](https://github.com/Mwaller129)

### [Trello Board](https://trello.com/b/yoiRt2Xh/showtime)

---

### **_Description_**

**A full-stack Django application allowing users to view, favorite, and review current Broadway shows.**

---

### **_Technologies_**

- Django
- PostgreSQL
- Python
- JavaScript
- HTML
- CSS

---

### **_About the App_**

#### Showtime is a Django web application designed as a central resource to help users track currently running Broadway shows. Once authenticated, users can review shows that they have seen and favorite shows that they want to attend. Users may also view details on Broadway venues, including a list of all shows currently playing at each venue.

#### Specifications (MVP):

- The home page provides the option to log in via Django authentication.
- Once authenticated, users can view an index of all currently running Broadway shows.
- Authenticated users can also view an index of Broadway theater venues.
- The detail page for each show lists basic details (title, director, location) and links to the detail page for the venue.
- The detail page for each venue displays the name and address of the venue, as well as a list of all shows currently running there.
- Authenticated users can leave reviews of shows they have seen. Reviews are visible to all authenticated users.

---

### **_Entity Relationship Diagram_**

#### ![Showtime ERD](/assets/Showtime%20ERD.png)
---

### **_Wireframes_**

#### ![A wireframe of the homepage](/assets/showtime_home.jpeg)
#### The Showtime homepage

#### ![A wireframe of the user's show list](/assets/user_show_list.jpeg)
#### The user's list of shows

#### ![A wireframe of the user's add review page](/assets/user_show_seen.jpeg)
#### The form to add a review of a show

#### ![A wireframe of the user's add show to wishlist page](/assets/user_show_desire.jpeg)
#### The form to add a show to a user's wishlist
---

### **_Stretch Goals (Post-MVP)_**

- [ ] The venue details page connects to an API to show the location of the venue on a map.
- [ ] On the show index page, users can search for a show by title.
- [ ] On the venue index page, users can search for a venue by name.
- [ ] On the show index page, shows that are no longer running are displayed at the bottom of the list and marked as inactive.
- [ ] The show index and venue index pages are limited to a certain number of entries on the first page, with additional pages added as necessary.

---

### **_Credits_**

##### To be added

