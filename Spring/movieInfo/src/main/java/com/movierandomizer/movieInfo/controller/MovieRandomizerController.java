package com.movierandomizer.movieInfo.controller;

import com.movierandomizer.movieInfo.Movie;
import com.movierandomizer.movieInfo.repository.MovieRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
// @AllArgsConstructor(onConstructor =@__(@Autowired))
@RequestMapping(path = "/movieRandomizer")
public class MovieRandomizerController {
    @Autowired
    private MovieRepository movieRepository;

    /* Add or update movie to db
        If movie exists we want to update the date field
            1st Check if there are multiple movies with the same name, if there are check the movieDirector
                Use getMovies method, check if response is empty

     */

    // Can I use put instead of post here? need ot use put with ID
        // Is there a way to get the count of movies in db since that is ID?
    @PutMapping(path = "/addMovie")
    public @ResponseBody String addNewMovie
            (
                    @RequestHeader(value = "movieName", required = true) String movieName,
                    @RequestHeader(value = "movieDirector", required = true) String movieDirector,
                    @RequestHeader(value = "movieYear", required = true) String movieYear,
                    @RequestHeader(value = "dateWatched", required = false) String dateWatched
            ){
        Movie movie = new Movie();
        movie.setMovieName(movieName);
        movie.setMovieDirector(movieDirector);
        movie.setMovieYear(movieYear);
        if (dateWatched != null) movie.setDateWatched(dateWatched);

        return "Movie added.";
    }

    /*
     This should return a list dependent on the header passed in
        If name, return all movie info with that name
        If director, return all movie info with director
        If year, return all movies from that year
        If dateWatched, return all movies watched that date
        No header, return list of all movies? Most recent 10?
            Add parameter with size, only return most recent 10 or size parameter
     */

    @GetMapping(path = "getMovies")
    public @ResponseBody String getMovie
}
