package com.movierandomizer.movieInfo.repository;

import org.springframework.data.repository.CrudRepository;
import com.movierandomizer.movieInfo.Movie;

public interface MovieRepository extends CrudRepository<Movie, Integer> {
}
