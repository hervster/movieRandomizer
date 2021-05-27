package com.movierandomizer.movieInfo;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Movie {
    @Id
    private Integer id;

    private String movieName, movieDirector, movieYear, dateWatched;

    // Getters
    public Integer getId() { return id; }
    public String getMovieName() { return movieName; }
    public String getMovieDirector() { return movieDirector; }
    public String getMovieYear() { return movieYear; }
    public String getDateWatched() { return dateWatched; }

    // Setters
    public void setDateWatched(String dateWatched) { this.dateWatched = dateWatched; }
    public void setId(Integer id) { this.id = id; }
    public void setMovieDirector(String movieDirector) { this.movieDirector = movieDirector; }
    public void setMovieName(String movieName) { this.movieName = movieName; }
    public void setMovieYear(String movieYear) { this.movieYear = movieYear; }
}
